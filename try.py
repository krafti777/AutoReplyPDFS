# import json
# from pyrogram import Client
# import asyncio
# from pyrogram.enums import ChatType
#
# app = Client("my_bot", bot_token="6701828344:AAETRWxuxfN4qIwzvxxKUWrkvN1hsg5hUbk", api_id="15601030",api_hash="3936d07bae0e18d0629547a068009f5b")
#
# async def get_chat_name(chat_id):
#     await app.start()
#     # ['username']
#     members = "["
#     async for member in app.get_chat_members(chat_id):
#         members += str(member) + ","
#     members = members[:-1];members += "]"
#
#     json_membs = (json.loads(members))
#
#     for member in json_membs:
#         user = member['user']
#         name = user.get('username')
#
#         print(f"Имя: {name}")
#
#     await app.stop()
#
# app.run(get_chat_name(-1001560934868))
import asyncio
from pyrogram import Client, filters
from parse import data
from pyrogram.parser import utils

app = Client("my_bot", api_id="28740688", api_hash="d8fbc7066c8fe6a96721bfb2161895cd")
CHAT_ID = [-1002422860800,-1002214908129,-1001560934868]
# def get_peer_type_new(peer_id: int) -> str:
#     peer_id_str = str(peer_id)
#     if not peer_id_str.startswith("-"):
#         return "user"
#     elif peer_id_str.startswith("-100"):
#         return "channel"
#     else:
#         return "chat"

# utils.get_peer_type = get_peer_type_new
titles = [item[1] for item in data]
print(data)
@app.on_message(filters.chat(CHAT_ID))
async def handle_new_message(client, message):
    print(message.chat.id)
    if str(message.text).strip()[0:5] == r"/book":
        set_titles_N_names = set()
        if str(message.text).lower() in titles:
            msg = str(message.text).lower()
            for ele in data:
                id,name = ele
                if name == msg:
                    item_sets = (id,name)
                    set_titles_N_names.add(item_sets)

        else:
            for el in str(message.text).lower().split():
                for title in titles:
                    for triger in str(title).lower().split(): #разбивка каждого тайтла на тригеры
                        if el == triger:
                            for ele in data: #
                                id,title_of_data = ele
                                if title_of_data == title:
                                    item_sets = (id,title_of_data)
                                    set_titles_N_names.add(item_sets)

        for element in set_titles_N_names:
            id,titleOfFile = element
            await app.send_document(message.chat.id, document=id,caption="Here ur file")
    # else:


app.run()

