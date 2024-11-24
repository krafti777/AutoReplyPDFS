from telethon import TelegramClient
import json

client = TelegramClient("my_bot_parse", api_id="26198465", api_hash="469cb911aa7e017429da7ceffb099584")

CHAT_ID = -1001560934868
HISTORY_CHAT_ID = -1002490130362

data = ""

async def get_chat_history():
    messages_in_file = "["
    async for message in client.iter_messages(HISTORY_CHAT_ID):
        messages_in_file += str(message) + ","
    messages_in_file = messages_in_file[:-1]
    messages_in_file += "]"

    json_members = json.loads(messages_in_file)

    listOfFiles = []
    for member in json_members:
        try:
            file_id = str(member.media.document.id)
            file_name = str(member.file.name).replace(".pdf","").strip().lower()
            listOfFile = listOfFiles.append([file_id, file_name])
        except:
            pass

    return listOfFiles

async def main():
    global data
    chat_history = await get_chat_history()
    data = chat_history

with client:
    client.loop.run_until_complete(main())