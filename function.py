from datetime import datetime
import random
import string
import pytz


def getTime() :
    japan_tz = pytz.timezone('Asia/Tokyo')
    current_time = datetime.now(japan_tz).strftime("%H%M")
    return current_time

def checkRarity(hhmm) :
    rarity = 0
    for char in hhmm:
        if char in ['0', '6', '9']:
            rarity += 1
        elif char == '8':
            rarity += 2
    return rarity

def getRandomNum(rarity) :
    if rarity == 0:
        return random.randint(1, 25)
    elif rarity == 1:
        return random.randint(26, 50)
    elif rarity == 2:
        return random.randint(51, 70)
    elif rarity == 3:
        return random.randint(71, 80)
    elif rarity == 4:
        return random.randint(81, 90)
    elif rarity == 5:
        return random.randint(91, 98)
    else:
        return random.randint(99, 100)

def randomResetCode() :
    resetCode = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    print(f'resetCode = {resetCode}')
    return resetCode

def getImageRarity(id):
    if id < 26:
        return 0
    elif id < 51:
        return 1
    elif id < 71:
        return 2
    elif id < 81:
        return 3
    elif id < 91:
        return 4
    elif id < 99:
        return 5
    elif id < 101:
        return 6
    else:
        return -1
