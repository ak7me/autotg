from pyrogram import Client
import pyrogram

import json
from time import sleep
from os import system, name

with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)


app = Client('NAME', config["api_id"], config["api_hash"])

def spam():
    try: 
        with app:
            while True:
                file = open('chats.txt')
                for line in file.readlines():
                    sleep(config["delay"])
                    app.send_message(app.get_chat(line[13:]).id, config["spam_text"])
                
                


    except Exception as exc:
        print(exc)


def main():
    system('cls' if name == 'nt' else 'clear')

    spam()
    app.run()


if __name__ == '__main__':
    main()