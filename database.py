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
             (id INTEGER PRIMARY KEY AUTOINCREMENT, answer_text TEXT, show_flag BOOLEAN, answer_flag BOOLEAN, image_name TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS reset_codes
    (reset_code TEXT)''')

c.execute("INSERT OR IGNORE INTO reset_codes (reset_code) VALUES (?)", ("reset",))

data = [
    { 'id': 1, 'answer_text': 'ROAD', 'showFlag': False , 'answerFlag': False, 'image_name': 'TBChJW6eUaaU.png'},
    { 'id': 2, 'answer_text': 'form', 'showFlag': False , 'answerFlag': False, 'image_name': 'FcJiJakY9GJz.png'},
    { 'id': 3, 'answer_text': 'lake', 'showFlag': False , 'answerFlag': False, 'image_name': 'xAxir2isqkan.png'},
    { 'id': 4, 'answer_text': 'true', 'showFlag': False , 'answerFlag': False, 'image_name': 'rHz6HbjDBkjc.png'},
    { 'id': 5, 'answer_text': 'REALIZE', 'showFlag': False , 'answerFlag': False, 'image_name': 'qct9vPGbUcRL.png'},
    { 'id': 6, 'answer_text': 'CODE', 'showFlag': False , 'answerFlag': False, 'image_name': 'M2743jPW2tkD.png'},
    { 'id': 7, 'answer_text': 'B', 'showFlag': False , 'answerFlag': False, 'image_name': 'sdjS7MKbqWKa.png'},
    { 'id': 8, 'answer_text': '20', 'showFlag': False , 'answerFlag': False, 'image_name': 'xTKbwpAVWih6.png'},
    { 'id': 9, 'answer_text': 'amazon', 'showFlag': False , 'answerFlag': False, 'image_name': 'e6HCZqGsgiAT.png'},
    { 'id': 10, 'answer_text': 'G', 'showFlag': False , 'answerFlag': False, 'image_name': 'mt8VPHEwhpdY.png'},
    { 'id': 11, 'answer_text': 'TOUR', 'showFlag': False , 'answerFlag': False, 'image_name': 'GC7xY7ngePyM.png'},
    { 'id': 12, 'answer_text': 'frog', 'showFlag': False , 'answerFlag': False, 'image_name': 'g9fWNyzqmcxP.png'},
    { 'id': 13, 'answer_text': 'ZOO', 'showFlag': False , 'answerFlag': False, 'image_name': 'dVHTcvs5XsJy.png'},
    { 'id': 14, 'answer_text': 'H', 'showFlag': False , 'answerFlag': False, 'image_name': 'wurqPPPCYKn7.png'},
    { 'id': 15, 'answer_text': 'JOKE', 'showFlag': False , 'answerFlag': False, 'image_name': 'EJPkiavyHLnW.png'},
    { 'id': 16, 'answer_text': 'she', 'showFlag': False , 'answerFlag': False, 'image_name': 'g5aXA3Db3BBT.png'},
    { 'id': 17, 'answer_text': 'Z', 'showFlag': False , 'answerFlag': False, 'image_name': 'NFRufZ8YVj69.png'},
    { 'id': 18, 'answer_text': '2', 'showFlag': False , 'answerFlag': False, 'image_name': 'RQGhhiv8NxU2.png'},
    { 'id': 19, 'answer_text': '9', 'showFlag': False , 'answerFlag': False, 'image_name': 'SDdBjRN7qmqr.png'},
    { 'id': 20, 'answer_text': 'use', 'showFlag': False , 'answerFlag': False, 'image_name': 'h9JZnDukuTFK.png'},
    { 'id': 21, 'answer_text': 'rock', 'showFlag': False , 'answerFlag': False, 'image_name': 'SGQkK6zLLi4u.png'},
    { 'id': 22, 'answer_text': 'story', 'showFlag': False , 'answerFlag': False, 'image_name': '6SwWbMywiTqC.png'},
    { 'id': 23, 'answer_text': 'BELT', 'showFlag': False , 'answerFlag': False, 'image_name': 'zDk0fkJTSZfj.png'},
    { 'id': 24, 'answer_text': 'onion', 'showFlag': False , 'answerFlag': False, 'image_name': '8apNNxnnDvme.png'},
    { 'id': 25, 'answer_text': 'star', 'showFlag': False , 'answerFlag': False, 'image_name': '379CR5XwvhXc.png'},
    { 'id': 26, 'answer_text': 'WORLD', 'showFlag': False , 'answerFlag': False, 'image_name': 'pFdC8i7Pa8av.png'},
    { 'id': 27, 'answer_text': 'RADIO', 'showFlag': False , 'answerFlag': False, 'image_name': 'pVRDLcU9ZEym.png'},
    { 'id': 28, 'answer_text': 'cloak', 'showFlag': False , 'answerFlag': False, 'image_name': '8mhcwPbnSAhe.png'},
    { 'id': 29, 'answer_text': 'MAZE', 'showFlag': False , 'answerFlag': False, 'image_name': 'zy8FUhA8nxuA.png'},
    { 'id': 30, 'answer_text': 'WITCH', 'showFlag': False , 'answerFlag': False, 'image_name': 'HnCbj3rLxbct.png'},
    { 'id': 31, 'answer_text': '14', 'showFlag': False , 'answerFlag': False, 'image_name': 'ujuvXDeD4air.png'},
    { 'id': 32, 'answer_text': 'song', 'showFlag': False , 'answerFlag': False, 'image_name': 'auY8twgNSkHH.png'},
    { 'id': 33, 'answer_text': 'piano', 'showFlag': False , 'answerFlag': False, 'image_name': 'GH9EL5e5nHjc.png'},
    { 'id': 34, 'answer_text': 'W', 'showFlag': False , 'answerFlag': False, 'image_name': 'fSqvqqmvtA5v.png'},
    { 'id': 35, 'answer_text': '14', 'showFlag': False , 'answerFlag': False, 'image_name': 'kPiEFU5ijDMB.png'},
    { 'id': 36, 'answer_text': 'angel', 'showFlag': False , 'answerFlag': False, 'image_name': 'JKk3G2v3kcNK.png'},
    { 'id': 37, 'answer_text': 'media', 'showFlag': False , 'answerFlag': False, 'image_name': 'hkufK5nkiRPD.png'},
    { 'id': 38, 'answer_text': 'G', 'showFlag': False , 'answerFlag': False, 'image_name': 'HfQc6sBKBXBD.png'},
    { 'id': 39, 'answer_text': 'heaven', 'showFlag': False , 'answerFlag': False, 'image_name': 'tvK83sZKwY9K.png'},
    { 'id': 40, 'answer_text': 'large', 'showFlag': False , 'answerFlag': False, 'image_name': 'xjyhXLV5VXkU.png'},
    { 'id': 41, 'answer_text': 'WINE', 'showFlag': False , 'answerFlag': False, 'image_name': 'Qm5zQqH5GiLj.png'},
    { 'id': 42, 'answer_text': 'DOG', 'showFlag': False , 'answerFlag': False, 'image_name': 'LN9PUFX7sKFF.png'},
    { 'id': 43, 'answer_text': 'past', 'showFlag': False , 'answerFlag': False, 'image_name': 'RMxi2TTt4MLQ.png'},
    { 'id': 44, 'answer_text': 'last', 'showFlag': False , 'answerFlag': False, 'image_name': '3TyBSzhqWqMZ.png'},
    { 'id': 45, 'answer_text': 'legend', 'showFlag': False , 'answerFlag': False, 'image_name': 'T4NhBA8MHkgS.png'},
    { 'id': 46, 'answer_text': 'CUT', 'showFlag': False , 'answerFlag': False, 'image_name': 'tFbRYM6z7eDh.png'},
    { 'id': 47, 'answer_text': '10', 'showFlag': False , 'answerFlag': False, 'image_name': 'nUhiTMmEeQK9.png'},
    { 'id': 48, 'answer_text': 'mind', 'showFlag': False , 'answerFlag': False, 'image_name': 'Ap7mmM9JhvnY.png'},
    { 'id': 49, 'answer_text': 'club', 'showFlag': False , 'answerFlag': False, 'image_name': 'h9LYQFeU4NNt.png'},
    { 'id': 50, 'answer_text': 'KNIGHT', 'showFlag': False , 'answerFlag': False, 'image_name': 'W6qbMyKC6cby.png'},
    { 'id': 51, 'answer_text': 'FLY', 'showFlag': False , 'answerFlag': False, 'image_name': 'yf9QfMLyxngk.png'},
    { 'id': 52, 'answer_text': 'jack', 'showFlag': False , 'answerFlag': False, 'image_name': 'pUFPDYLjsG2m.png'},
    { 'id': 53, 'answer_text': 'season', 'showFlag': False , 'answerFlag': False, 'image_name': 'bvMs8SGdV6JD.png'},
    { 'id': 54, 'answer_text': 'toy', 'showFlag': False , 'answerFlag': False, 'image_name': 'TxK8x56Er6yz.png'},
    { 'id': 55, 'answer_text': 'BASE', 'showFlag': False , 'answerFlag': False, 'image_name': 'P3DHfBT5pVwj.png'},
    { 'id': 56, 'answer_text': 'snake', 'showFlag': False , 'answerFlag': False, 'image_name': 'RDQNCGuNDB9Q.png'},
    { 'id': 57, 'answer_text': 'SKY', 'showFlag': False , 'answerFlag': False, 'image_name': 'kvNT2aF6ssYv.png'},
    { 'id': 58, 'answer_text': 'FOXTROT', 'showFlag': False , 'answerFlag': False, 'image_name': 'geHvqLY4dDVm.png'},
    { 'id': 59, 'answer_text': 'JAIL', 'showFlag': False , 'answerFlag': False, 'image_name': 'Wq7BhtNXi9EK.png'},
    { 'id': 60, 'answer_text': 'air', 'showFlag': False , 'answerFlag': False, 'image_name': 'Sx62AdeSSUvd.png'},
    { 'id': 61, 'answer_text': 'bear', 'showFlag': False , 'answerFlag': False, 'image_name': 'tYN8VM9vN37N.png'},
    { 'id': 62, 'answer_text': 'mild', 'showFlag': False , 'answerFlag': False, 'image_name': 'teTGsbywy33W.png'},
    { 'id': 63, 'answer_text': 'VIOLET', 'showFlag': False , 'answerFlag': False, 'image_name': 'nBDbxnaxgx3X.png'},
    { 'id': 64, 'answer_text': 'maize', 'showFlag': False , 'answerFlag': False, 'image_name': '6rGNmcQ6MsNz.png'},
    { 'id': 65, 'answer_text': 'ace', 'showFlag': False , 'answerFlag': False, 'image_name': 'vj46dvQ6YvkH.png'},
    { 'id': 66, 'answer_text': 'stay', 'showFlag': False , 'answerFlag': False, 'image_name': 'RwGzbaV3APwA.png'},
    { 'id': 67, 'answer_text': 'BELL', 'showFlag': False , 'answerFlag': False, 'image_name': 'ZhwvsBx6SDrX.png'},
    { 'id': 68, 'answer_text': 'push', 'showFlag': False , 'answerFlag': False, 'image_name': 'PvHs2y6cED83.png'},
    { 'id': 69, 'answer_text': 'bar', 'showFlag': False , 'answerFlag': False, 'image_name': 'sMjBB7UCjxQx.png'},
    { 'id': 70, 'answer_text': 'magic', 'showFlag': False , 'answerFlag': False, 'image_name': 'SkGRHjQzj2dv.png'},
    { 'id': 71, 'answer_text': 'AQUA', 'showFlag': False , 'answerFlag': False, 'image_name': 'NhrhW2JYuDP9.png'},
    { 'id': 72, 'answer_text': 'pigeon', 'showFlag': False , 'answerFlag': False, 'image_name': '5xWAUi4BN2ab.png'},
    { 'id': 73, 'answer_text': 'crab', 'showFlag': False , 'answerFlag': False, 'image_name': 'pfifzEHr4cUP.png'},
    { 'id': 74, 'answer_text': 'EAGLE', 'showFlag': False , 'answerFlag': False, 'image_name': 'Cd7pFrdhvNnE.png'},
    { 'id': 75, 'answer_text': '19', 'showFlag': False , 'answerFlag': False, 'image_name': 'F43NBm7TFLZT.png'},
    { 'id': 76, 'answer_text': 'dive', 'showFlag': False , 'answerFlag': False, 'image_name': 'gfQuxY8EBueW.png'},
    { 'id': 77, 'answer_text': 'tag', 'showFlag': False , 'answerFlag': False, 'image_name': '7XxUjkk6FNpk.png'},
    { 'id': 78, 'answer_text': 'spy', 'showFlag': False , 'answerFlag': False, 'image_name': 'Vz9X7xp2D3BK.png'},
    { 'id': 79, 'answer_text': 'BATH', 'showFlag': False , 'answerFlag': False, 'image_name': '3TKpNhVpsb8Y.png'},
    { 'id': 80, 'answer_text': 'step', 'showFlag': False , 'answerFlag': False, 'image_name': 'LdCUtbC7dEYZ.png'},
    { 'id': 81, 'answer_text': 'bag', 'showFlag': False , 'answerFlag': False, 'image_name': 'SVG93iJjNm39.png'},
    { 'id': 82, 'answer_text': 'n', 'showFlag': False , 'answerFlag': False, 'image_name': 'dnF2XraxLAc9.png'},
    { 'id': 83, 'answer_text': 'ROSE', 'showFlag': False , 'answerFlag': False, 'image_name': '9KXRyA7ij9rH.png'},
    { 'id': 84, 'answer_text': 'evil', 'showFlag': False , 'answerFlag': False, 'image_name': 'dFTNSeV0QmWk.png'},
    { 'id': 85, 'answer_text': 'I', 'showFlag': False , 'answerFlag': False, 'image_name': 'w5U9ruyqPvep.png'},
    { 'id': 86, 'answer_text': 'GHOST', 'showFlag': False , 'answerFlag': False, 'image_name': 'A3WmxdNGViHA.png'},
    { 'id': 87, 'answer_text': 'TRAIN', 'showFlag': False , 'answerFlag': False, 'image_name': 'Ng3gTSGEq4y7.png'},
    { 'id': 88, 'answer_text': 'knock', 'showFlag': False , 'answerFlag': False, 'image_name': '7c8SFFB6Yuxe.png'},
    { 'id': 89, 'answer_text': 'Z', 'showFlag': False , 'answerFlag': False, 'image_name': '4Enb7gMvG7gL.png'},
    { 'id': 90, 'answer_text': 'CROWN', 'showFlag': False , 'answerFlag': False, 'image_name': '7dwWEDN7ceXQ.png'},
    { 'id': 91, 'answer_text': 'long', 'showFlag': False , 'answerFlag': False, 'image_name': '2jnDyXBBa8vv.png'},
    { 'id': 92, 'answer_text': 'library', 'showFlag': False , 'answerFlag': False, 'image_name': 'vA4D2mzsvHvG.png'},
    { 'id': 93, 'answer_text': 'PICTURE', 'showFlag': False , 'answerFlag': False, 'image_name': 'Nz9hCD6r6Hpb.png'},
    { 'id': 94, 'answer_text': 'GET', 'showFlag': False , 'answerFlag': False, 'image_name': '7XNH2NHW3Zua.png'},
    { 'id': 95, 'answer_text': 'VINEGER', 'showFlag': False , 'answerFlag': False, 'image_name': 'Jbcr93wZNrrh.png'},
    { 'id': 96, 'answer_text': '55', 'showFlag': False , 'answerFlag': False, 'image_name': 'pfsNMCiLsZ46.png'},
    { 'id': 97, 'answer_text': 'OZONE', 'showFlag': False , 'answerFlag': False, 'image_name': 'vRw4XGx2Abad.png'},
    { 'id': 98, 'answer_text': 'X', 'showFlag': False , 'answerFlag': False, 'image_name': 'XqARpF7Q3jvZ.png'},
    { 'id': 99, 'answer_text': 'JAM', 'showFlag': False , 'answerFlag': False, 'image_name': 'hGGk9nQMP6hS.png'},
    { 'id': 100, 'answer_text': 'virus', 'showFlag': False , 'answerFlag': False, 'image_name': 'LBq5JWpYdCyK.png'},
]
for item in data:
    c.execute("INSERT INTO answers (answer_text, show_flag, answer_flag, image_name) VALUES (?, ?, ?, ?)",
              (item['answer_text'], item['showFlag'], item['answerFlag'], item['image_name']))

# 変更を確定する
conn.commit()

# DBとの接続を閉じる
conn.close()