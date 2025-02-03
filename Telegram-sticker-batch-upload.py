from telethon.sync import TelegramClient
from telethon.tl.types import InputFile
import asyncio
import os

async def add_to_existing_sticker_set(api_id, api_hash, sticker_folder):
    async with TelegramClient('sticker_uploader', api_id, api_hash) as client:
        print("Successfully connected to Telegram!")
        
        # 连接到 @Stickers bot
        stickers_bot = await client.get_entity('@Stickers')
        
        # 发送 /addsticker 命令
        await client.send_message(stickers_bot, '/addsticker')
        await asyncio.sleep(2)
        
        # 发送现有贴纸包的短名称
        await client.send_message(stickers_bot, 'xqhxm_1')
        await asyncio.sleep(2)
        
        # 上传每个贴纸
        for file in os.listdir(sticker_folder):
            # 检查是否为 PNG 或 WEBP 格式
            if file.endswith(('.png', '.webp')):
                file_path = os.path.join(sticker_folder, file)
                print(f"Uploading {file}...")
                
                # 以文件形式发送
                await client.send_file(
                    stickers_bot,
                    file_path,
                    force_document=True,
                    allow_cache=False,
                )
                await asyncio.sleep(2)
                
                # 发送表情符号
                await client.send_message(stickers_bot, '🌟')
                await asyncio.sleep(2)
        
        # 完成添加
        await client.send_message(stickers_bot, '/done')
        print("Stickers added successfully to existing pack!")

if __name__ == '__main__':
    # Telegram API 凭据
    API_ID = ''  # 从 my.telegram.org 获取
    API_HASH = ''  # 从 my.telegram.org 获取
    STICKER_FOLDER = '/root/EmojiPackage/123_telegram'  # 贴纸文件夹路径
    
    # 运行上传程序
    asyncio.run(add_to_existing_sticker_set(API_ID, API_HASH, STICKER_FOLDER))
