# database.py
import sqlite3

# DBに接続する
conn = sqlite3.connect('quiz.db')
c = conn.cursor()

# ユーザーテーブルを作成する
c.execute('''CREATE TABLE IF NOT EXISTS users
             (user_id TEXT PRIMARY KEY, timestamp DATETIME, last_draw_time DATETIME)''')

# 解答履歴テーブルを作成する
c.execute('''CREATE TABLE IF NOT EXISTS answers
             (id INTEGER PRIMARY KEY AUTOINCREMENT, answer_text TEXT, show_flag BOOLEAN, answer_flag BOOLEAN)''')

c.execute('''CREATE TABLE IF NOT EXISTS reset_codes
    (reset_code TEXT)''')

c.execute("INSERT OR IGNORE INTO reset_codes (reset_code) VALUES (?)", ("reset",))

data = [
    { 'id': 1, 'answer_text': 'ROAD', 'showFlag': False , 'answerFlag': False,},
    { 'id': 2, 'answer_text': 'form', 'showFlag': False , 'answerFlag': False},
    { 'id': 3, 'answer_text': 'lake', 'showFlag': False , 'answerFlag': False},
    { 'id': 4, 'answer_text': 'true', 'showFlag': False , 'answerFlag': False},
    { 'id': 5, 'answer_text': 'REALIZE', 'showFlag': False , 'answerFlag': False},
    { 'id': 6, 'answer_text': 'CODE', 'showFlag': False , 'answerFlag': False},
    { 'id': 7, 'answer_text': 'B', 'showFlag': False , 'answerFlag': False},
    { 'id': 8, 'answer_text': '20', 'showFlag': False , 'answerFlag': False},
    { 'id': 9, 'answer_text': 'amazon', 'showFlag': False , 'answerFlag': False},
    { 'id': 10, 'answer_text': 'G', 'showFlag': False , 'answerFlag': False},
    { 'id': 11, 'answer_text': 'TOUR', 'showFlag': False , 'answerFlag': False},
    { 'id': 12, 'answer_text': 'frog', 'showFlag': False , 'answerFlag': False},
    { 'id': 13, 'answer_text': 'ZOO', 'showFlag': False , 'answerFlag': False},
    { 'id': 14, 'answer_text': 'H', 'showFlag': False , 'answerFlag': False},
    { 'id': 15, 'answer_text': 'JOKE', 'showFlag': False , 'answerFlag': False},
    { 'id': 16, 'answer_text': 'she', 'showFlag': False , 'answerFlag': False},
    { 'id': 17, 'answer_text': 'Z', 'showFlag': False , 'answerFlag': False},
    { 'id': 18, 'answer_text': '2', 'showFlag': False , 'answerFlag': False},
    { 'id': 19, 'answer_text': '9', 'showFlag': False , 'answerFlag': False},
    { 'id': 20, 'answer_text': 'use', 'showFlag': False , 'answerFlag': False},
    { 'id': 21, 'answer_text': 'rock', 'showFlag': False , 'answerFlag': False},
    { 'id': 22, 'answer_text': 'story', 'showFlag': False , 'answerFlag': False},
    { 'id': 23, 'answer_text': 'BELT', 'showFlag': False , 'answerFlag': False},
    { 'id': 24, 'answer_text': 'onion', 'showFlag': False , 'answerFlag': False},
    { 'id': 25, 'answer_text': 'star', 'showFlag': False , 'answerFlag': False},
    { 'id': 26, 'answer_text': 'WORLD', 'showFlag': False , 'answerFlag': False},
    { 'id': 27, 'answer_text': 'RADIO', 'showFlag': False , 'answerFlag': False},
    { 'id': 28, 'answer_text': 'cloak', 'showFlag': False , 'answerFlag': False},
    { 'id': 29, 'answer_text': 'MAZE', 'showFlag': False , 'answerFlag': False},
    { 'id': 30, 'answer_text': 'WITCH', 'showFlag': False , 'answerFlag': False},
    { 'id': 31, 'answer_text': '14', 'showFlag': False , 'answerFlag': False},
    { 'id': 32, 'answer_text': 'song', 'showFlag': False , 'answerFlag': False},
    { 'id': 33, 'answer_text': 'piano', 'showFlag': False , 'answerFlag': False},
    { 'id': 34, 'answer_text': 'W', 'showFlag': False , 'answerFlag': False},
    { 'id': 35, 'answer_text': '14', 'showFlag': False , 'answerFlag': False},
    { 'id': 36, 'answer_text': 'angel', 'showFlag': False , 'answerFlag': False},
    { 'id': 37, 'answer_text': 'media', 'showFlag': False , 'answerFlag': False},
    { 'id': 38, 'answer_text': 'G', 'showFlag': False , 'answerFlag': False},
    { 'id': 39, 'answer_text': 'heaven', 'showFlag': False , 'answerFlag': False},
    { 'id': 40, 'answer_text': 'large', 'showFlag': False , 'answerFlag': False},
    { 'id': 41, 'answer_text': 'WINE', 'showFlag': False , 'answerFlag': False},
    { 'id': 42, 'answer_text': 'DOG', 'showFlag': False , 'answerFlag': False},
    { 'id': 43, 'answer_text': 'past', 'showFlag': False , 'answerFlag': False},
    { 'id': 44, 'answer_text': 'last', 'showFlag': False , 'answerFlag': False},
    { 'id': 45, 'answer_text': 'legend', 'showFlag': False , 'answerFlag': False},
    { 'id': 46, 'answer_text': 'CUT', 'showFlag': False , 'answerFlag': False},
    { 'id': 47, 'answer_text': '10', 'showFlag': False , 'answerFlag': False},
    { 'id': 48, 'answer_text': 'mind', 'showFlag': False , 'answerFlag': False},
    { 'id': 49, 'answer_text': 'club', 'showFlag': False , 'answerFlag': False},
    { 'id': 50, 'answer_text': 'KNIGHT', 'showFlag': False , 'answerFlag': False},
    { 'id': 51, 'answer_text': 'FLY', 'showFlag': False , 'answerFlag': False},
    { 'id': 52, 'answer_text': 'jack', 'showFlag': False , 'answerFlag': False},
    { 'id': 53, 'answer_text': 'season', 'showFlag': False , 'answerFlag': False},
    { 'id': 54, 'answer_text': 'toy', 'showFlag': False , 'answerFlag': False},
    { 'id': 55, 'answer_text': 'BASE', 'showFlag': False , 'answerFlag': False},
    { 'id': 56, 'answer_text': 'snake', 'showFlag': False , 'answerFlag': False},
    { 'id': 57, 'answer_text': 'SKY', 'showFlag': False , 'answerFlag': False},
    { 'id': 58, 'answer_text': 'FOXTROT', 'showFlag': False , 'answerFlag': False},
    { 'id': 59, 'answer_text': 'JAIL', 'showFlag': False , 'answerFlag': False},
    { 'id': 60, 'answer_text': 'air', 'showFlag': False , 'answerFlag': False},
    { 'id': 61, 'answer_text': 'bear', 'showFlag': False , 'answerFlag': False},
    { 'id': 62, 'answer_text': 'mild', 'showFlag': False , 'answerFlag': False},
    { 'id': 63, 'answer_text': 'VIOLET', 'showFlag': False , 'answerFlag': False},
    { 'id': 64, 'answer_text': 'maize', 'showFlag': False , 'answerFlag': False},
    { 'id': 65, 'answer_text': 'ace', 'showFlag': False , 'answerFlag': False},
    { 'id': 66, 'answer_text': 'stay', 'showFlag': False , 'answerFlag': False},
    { 'id': 67, 'answer_text': 'BELL', 'showFlag': False , 'answerFlag': False},
    { 'id': 68, 'answer_text': 'push', 'showFlag': False , 'answerFlag': False},
    { 'id': 69, 'answer_text': 'bar', 'showFlag': False , 'answerFlag': False},
    { 'id': 70, 'answer_text': 'magic', 'showFlag': False , 'answerFlag': False},
    { 'id': 71, 'answer_text': 'AQUA', 'showFlag': False , 'answerFlag': False},
    { 'id': 72, 'answer_text': 'pigeon', 'showFlag': False , 'answerFlag': False},
    { 'id': 73, 'answer_text': 'crab', 'showFlag': False , 'answerFlag': False},
    { 'id': 74, 'answer_text': 'EAGLE', 'showFlag': False , 'answerFlag': False},
    { 'id': 75, 'answer_text': '19', 'showFlag': False , 'answerFlag': False},
    { 'id': 76, 'answer_text': 'dive', 'showFlag': False , 'answerFlag': False},
    { 'id': 77, 'answer_text': 'tag', 'showFlag': False , 'answerFlag': False},
    { 'id': 78, 'answer_text': 'spy', 'showFlag': False , 'answerFlag': False},
    { 'id': 79, 'answer_text': 'BATH', 'showFlag': False , 'answerFlag': False},
    { 'id': 80, 'answer_text': 'step', 'showFlag': False , 'answerFlag': False},
    { 'id': 81, 'answer_text': 'bag', 'showFlag': False , 'answerFlag': False},
    { 'id': 82, 'answer_text': 'n', 'showFlag': False , 'answerFlag': False},
    { 'id': 83, 'answer_text': 'ROSE', 'showFlag': False , 'answerFlag': False},
    { 'id': 84, 'answer_text': 'evil', 'showFlag': False , 'answerFlag': False},
    { 'id': 85, 'answer_text': 'I', 'showFlag': False , 'answerFlag': False},
    { 'id': 86, 'answer_text': 'GHOST', 'showFlag': False , 'answerFlag': False},
    { 'id': 87, 'answer_text': 'TRAIN', 'showFlag': False , 'answerFlag': False},
    { 'id': 88, 'answer_text': 'knock', 'showFlag': False , 'answerFlag': False},
    { 'id': 89, 'answer_text': 'Z', 'showFlag': False , 'answerFlag': False},
    { 'id': 90, 'answer_text': 'CROWN', 'showFlag': False , 'answerFlag': False},
    { 'id': 91, 'answer_text': 'long', 'showFlag': False , 'answerFlag': False},
    { 'id': 92, 'answer_text': 'library', 'showFlag': False , 'answerFlag': False},
    { 'id': 93, 'answer_text': 'PICTURE', 'showFlag': False , 'answerFlag': False},
    { 'id': 94, 'answer_text': 'GET', 'showFlag': False , 'answerFlag': False},
    { 'id': 95, 'answer_text': 'VINEGER', 'showFlag': False , 'answerFlag': False},
    { 'id': 96, 'answer_text': '55', 'showFlag': False , 'answerFlag': False},
    { 'id': 97, 'answer_text': 'OZONE', 'showFlag': False , 'answerFlag': False},
    { 'id': 98, 'answer_text': 'X', 'showFlag': False , 'answerFlag': False},
    { 'id': 99, 'answer_text': 'JAM', 'showFlag': False , 'answerFlag': False},
    { 'id': 100, 'answer_text': 'virus', 'showFlag': False , 'answerFlag': False},
]
for item in data:
    c.execute("INSERT INTO answers (answer_text, show_flag, answer_flag) VALUES (?, ?, ?)",
              (item['answer_text'], item['showFlag'], item['answerFlag']))

# 変更を確定する
conn.commit()

# DBとの接続を閉じる
conn.close()