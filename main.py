import os
import sqlite3
import datetime
from dotenv import load_dotenv

from function import getTime, checkRarity, getRandomNum, randomResetCode

from flask import Flask, abort, request
from linebot.v3.webhook import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    ImageMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
app = Flask(__name__)

load_dotenv()
# WebhookHandler のトークンを環境変数から取得
webhook_handler_token = os.getenv('LINE_CHANNEL_SECRET')
# Configuration のアクセストークンを環境変数から取得
configuration_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
# WebhookHandler を設定
handler = WebhookHandler(webhook_handler_token)
# Configuration を設定
configuration = Configuration(access_token=configuration_access_token)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):

    with ApiClient(configuration) as api_client:

        conn = sqlite3.connect('quiz.db')
        c = conn.cursor()
        c.execute("SELECT reset_code FROM reset_codes")
        resetCode = c.fetchone()[0]
        c.execute("SELECT COUNT(*) FROM answers WHERE show_flag = 1")
        show_flag_count = c.fetchone()[0]
        c.execute("SELECT COUNT(*) FROM answers WHERE answer_flag = 1")
        answer_flag_count = c.fetchone()[0]
        c.execute("SELECT id FROM answers WHERE show_flag = 1")
        public_questions = [row[0] for row in c.fetchall()]
        c.execute("SELECT id FROM answers WHERE answer_flag = 1")
        correct_answers = [row[0] for row in c.fetchall()]
        conn.close()

        #相手の送信した内容で条件分岐して回答を変数に代入
        if event.message.text == 'ドロー':
                user_id = event.source.user_id
                conn = sqlite3.connect('quiz.db')
                c = conn.cursor()
                
                # ユーザーが存在しない場合は新規登録
                c.execute("INSERT OR IGNORE INTO users (user_id, timestamp) VALUES (?, ?)", (user_id, datetime.datetime.now()))
                
                # 最終ドロー時間を取得
                c.execute("SELECT last_draw_time FROM users WHERE user_id = ?", (user_id,))
                last_draw_time_str = c.fetchone()[0]
                
                # last_draw_timeがNoneでない場合は、datetime型に変換
                if last_draw_time_str:
                    last_draw_time = datetime.datetime.strptime(last_draw_time_str, '%Y-%m-%d %H:%M:%S.%f')
                else:
                    last_draw_time = None
                
                rarity = None  # rarityを初期化
                imageNum = None  # imageNumも初期化
                
                # 1時間以内にドローされていた場合
                if last_draw_time and (datetime.datetime.now() - last_draw_time) < datetime.timedelta(hours=1):
                    wait_time = datetime.timedelta(hours=1) - (datetime.datetime.now() - last_draw_time)
                    msg = f"1時間以内にドローされています。あと{wait_time.seconds // 60}分{wait_time.seconds % 60}秒待ってから再度ドローしてください。"
                    line_bot_api = MessagingApi(api_client)
                    line_bot_api.reply_message_with_http_info(
                        ReplyMessageRequest(
                            reply_token=event.reply_token,
                            messages=[
                                TextMessage(text=msg)
                            ]
                        )
                    )
                else:
                    # ドロー処理
                    hhmm = getTime()
                    rarity = checkRarity(hhmm)
                    imageNum = getRandomNum(rarity)
                    msg = f'ドローしました:rarity{rarity}'
                    
                    # 最終ドロー時間を更新
                    c.execute("UPDATE users SET last_draw_time = ? WHERE user_id = ?", (datetime.datetime.now(), user_id))
                    # answersテーブルからid:imageNumのレコードを取得,show_flagが0の場合はshow_flagを1に更新
                    c.execute("SELECT * FROM answers WHERE id = ? AND show_flag = 0", (imageNum,))
                    answer = c.fetchone()
                    if answer:
                        c.execute("UPDATE answers SET show_flag = 1 WHERE id = ?", (imageNum,))
                    conn.commit()
                
                conn.close()

                if rarity is not None and imageNum is not None:
                    line_bot_api = MessagingApi(api_client)
                    line_bot_api.reply_message_with_http_info(
                        ReplyMessageRequest(
                            reply_token=event.reply_token,
                            messages=[
                                TextMessage(text=msg),
                                ImageMessage(
                                    type='image',
                                    original_content_url=f'https://nazo100bot-site.vercel.app/img/{str(rarity)}/{str(imageNum)}.png',
                                    preview_image_url=f'https://nazo100bot-site.vercel.app/img/{str(rarity)}/{str(imageNum)}.png'
                                )
                            ]
                        )
                    )

        elif event.message.text == resetCode and show_flag_count == 100 and answer_flag_count == 100:
            msg = 'クリアです!!\n問題の正解数がリセットされました'
            resetCode = randomResetCode()
            conn = sqlite3.connect('quiz.db')
            c = conn.cursor()
            c.execute("UPDATE reset_codes SET reset_code = ?", (resetCode,))
            c.execute("UPDATE answers SET show_flag = 0, answer_flag = 0")
            conn.commit()
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        TextMessage(text=msg)
                    ]
                )
            )
            
        elif '-' in event.message.text:
            # -の左右で分割
            answer_id, answer_text = event.message.text.split('-')
            conn = sqlite3.connect('quiz.db')
            c = conn.cursor()
            c.execute("SELECT answer_text FROM answers WHERE id = ?", (answer_id,))
            correct_answer = c.fetchone()[0]
            c.execute("SELECT show_flag FROM answers WHERE id = ?", (answer_id,))
            show_flag = c.fetchone()[0]
            conn.close()

            if answer_text == correct_answer and show_flag == 1:
                conn = sqlite3.connect('quiz.db')
                c = conn.cursor()
                c.execute("UPDATE answers SET answer_flag = 1 WHERE id = ?", (answer_id,))
                conn.commit()
                conn.close()
                msg = '正解です'
                line_bot_api = MessagingApi(api_client)
                line_bot_api.reply_message_with_http_info(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=msg)
                        ]
                    )
                )
            else:
                msg = '不正解/問題が未公開です'
                line_bot_api = MessagingApi(api_client)
                line_bot_api.reply_message_with_http_info(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=msg)
                        ]
                    )
                )
            
        elif event.message.text == '情報':
            msg = f'公開済み問題数:{show_flag_count}\n{public_questions}\n正解数:{answer_flag_count}\n{correct_answers}'
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        TextMessage(text=msg)
                    ]
                )
            )

        elif event.message.text == 'その他':
            msg = ''
            msg = 'このコンテンツは「Project:;COLD 2.0 ALTÆR CARNIVAL」二次利用ガイドラインに沿って公開をしています。\n\n'
            msg += '◆二次利用元：\n[二次利用元の対象コンテンツのURLを入力・複数でも可]\n\n'
            msg += '◆「Project:;COLD 2.0 ALTÆR CARNIVAL」関連情報：\n'
            msg += '公式サイト：https://bit.ly/3u5BYM3\n'
            msg += 'YouTube：https://bit.ly/5YuuN42\n'
            msg += 'X：https://bit.ly/3HvvKbl\n'
            msg += '公式Discord：https://bit.ly/3vRhaZl\n\n'
            msg += '◆二次利用関連情報：\n'
            msg += '「 Project:;COLD 2.0 ALTÆR CARNIVAL」二次利用ガイドライン：https://bit.ly/3SDfXwy\n'
            msg += '不正利用の通報：https://bit.ly/3KTtjiJ\n'
            msg += '著作物ID：#A000000000002839\n'
            msg += '利用許諾協力：#クリエイターサポートプログラム\n'
            msg += 'CSP（クリエイターサポートプログラム）公式X：https://bit.ly/3zXvoYF\n'
            msg += 'お問い合わせ：csp-info@ml.kadokawa.jp'
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        TextMessage(text=msg)
                    ]
                )
            )

        else:
            msg = '対応してません'
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        TextMessage(text=msg)
                    ]
                )
            )

        if show_flag_count == 100 and answer_flag_count == 100:
            msg = f'全問正解しました!!\nクリアコードは{resetCode}です'
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        TextMessage(text=msg)
                    ]
                )
            )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=False)
