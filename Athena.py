import os, glob, random
from configparser import ConfigParser
from telethon import TelegramClient
import huepy
config = ConfigParser()
config.read('Config.cfg')
api_id = int(config['telegram']['api_id'])
api_hash = config['telegram']['api_hash']
print('''______________¶¶¶
_____________¶¶_¶¶¶¶
____________¶¶____¶¶¶
___________¶¶¶______¶¶
___________¶¶¶_______¶¶
__________¶¶¶¶________¶¶
__________¶_¶¶_________¶¶
__________¶__¶¶_________¶¶____¶¶
__________¶__¶¶__________¶¶¶¶¶¶¶
_________¶¶__¶¶¶______¶¶¶¶¶¶___¶
_________¶¶___¶¶__¶¶¶¶¶¶__¶¶
_______¶¶_¶____¶¶¶¶________¶¶
______¶¶__¶¶___¶¶__________¶¶
_____¶¶____¶¶___¶¶__________¶¶
___¶¶_______¶¶___¶¶_________¶¶
___¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶_________¶
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶________¶¶
¶¶__¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶______¶¶
¶¶¶¶¶___¶______¶___¶¶¶¶¶_____¶¶
________¶¶¶¶¶¶¶¶______¶¶¶¶¶_¶¶
______¶¶¶¶¶¶¶¶¶¶¶________¶¶¶¶
______¶¶¶¶¶¶¶¶¶¶¶¶
______¶__¶¶_¶¶¶¶¶¶
_____¶¶______¶___¶      Simple Telegram Spamming Client
_____¶¶_____¶¶___¶
_____¶______¶¶___¶      \u001b[38;5;3m[!]\u001b[0m Don't use too often, it can lead to limiting your account
____¶¶______¶¶___¶¶     To get started:
____¶¶______¶¶___¶¶     1. Replace pictures in jpg / png format in the Pictures folder
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶     2. Go to https://my.telegram.org and create Application
__¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶    3. Copy api_id and api_hash into config.cfg
__¶¶________¶¶¶____¶¶   4. Run script and create session
____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶''')
print("\u001b[38;5;63m[*]\u001b[0m Using API_ID " + str(api_id))
print("\u001b[38;5;63m[*]\u001b[0m Using API_HASH " + api_hash)
client = TelegramClient('session', api_id, api_hash)


def randomize(k):
    if k == 1:
        lines = open('Phrases.txt').read().splitlines()
        upload_text = random.choice(lines)
    else:
        upload_text = ''
    return upload_text


async def sendimages(bot_name, randomize, k):
    for jpgfile in glob.iglob(os.path.join("Pictures", "*.jpg")):
        print("\u001b[38;5;63m[*]\u001b[0m Sending " + jpgfile)
        await client.send_file(bot_name, jpgfile, caption=randomize(k))
    for pngfile in glob.iglob(os.path.join("Pictures", "*.png")):
        print("\u001b[38;5;63m[*]\u001b[0m Sending " + pngfile)
        await client.send_file(bot_name, pngfile, caption=randomize(k))
    print("\u001b[38;5;63m[*]\u001b[0m Done")


async def initialize(k):
    print("\u001b[38;5;63m[*]\u001b[0m Select what do you want to spam")
    print("\u001b[0m[1] Bot")
    print("\u001b[0m[2] User")
    option = input("\u001b[31mAthena \u001b[0m> ")
    print("\u001b[38;5;63m[*]\u001b[0m Enter Target Name without using @. Example: armyrusBOT")
    bot_name = input("\u001b[31mAthena \u001b[0m> ")

    while 1:
        if option == '1':
            try:
                await client.send_message(bot_name, '/start')
                break
            except:
                await main()
        elif option == '2':
            try:
                break
            except:
                await main()
        else:
            print("\u001b[38;5;63m[*]\u001b[0m Incorrect input")
            await main()
    print("\u001b[38;5;63m[*]\u001b[0m Do you want to use random phrases from a file y/N ?")
    fileusage = input("\u001b[31mAthena \u001b[0m> ")
    while 1:
        if fileusage == 'y' or fileusage == 'Y':
            try:
                k = 1
                await sendimages(bot_name, randomize, k)
                break
            except:
                await main()
        elif fileusage == 'n' or fileusage == 'N':
            try:
                k = 0
                await sendimages(bot_name, randomize, k)
                break
            except:
                await main()
        else:
            print("\u001b[38;5;63m[*]\u001b[0m Incorrect input")
            await main()
    input("\u001b[38;5;63m[*]\u001b[0m Press Enter to choose another target")
    await initialize(k)


with client:
    client.loop.run_until_complete(initialize(k=0))


async def main():
    await initialize()

