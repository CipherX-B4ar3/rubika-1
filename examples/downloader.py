
import asyncio
import logging
import aiohttp
import mimetypes
from urllib.parse import unquote
from rubika import Client, models, handlers

logging.basicConfig(level=logging.ERROR)


def progress_bar(total, index):
    filled = int(index * 15 / total)
    progress = '|'
    progress += '█' * filled
    progress += '-' * (15 - filled)
    progress += '| ▅▃▁'
    progress += f' [{int(index * 100 / total):,}%]'
    return progress


async def main():
    async with Client(session='rubika') as client:
        @client.on(handlers.MessageUpdates(models.RegexModel(r'^dl (\S+)$')))
        async def updates(update):
            try:
                url = unquote(update.pattern_match.group(1))
                async with aiohttp.ClientSession() as session:
                    result = b''
                    async with session.get(url) as respond:
                        length = int(respond.headers.get('Content-Length'))
                        chunk = length // 15
                        message = await update.reply(
                            'در حال **دانلود فایل** ...')
                        async for part in respond.content.iter_chunked(chunk):
                            result += part
                            await message.edit(
                                'در حال **دانلود فایل** ...\n\n'
                                + progress_bar(length, len(result)))

                async def callback(total, index):
                    await message.edit('در حال **آپلود فایل** ...\n\n'
                                    + progress_bar(total, index))

                mime = mimetypes.guess_type(url)
                is_image = False
                is_music = False
                is_video = False
                if mime is not None:
                    if 'audio' in mime[0]:
                        is_music = True

                    elif 'image' in mime[0]:
                        is_image = True

                    elif 'video' in mime[0]:
                        is_video = True

                await update.reply(chunk=chunk,
                                   is_music=is_music,
                                   is_image=is_image,
                                   is_video=is_video,
                                   callback=callback,
                                   file_inline=result,
                                   file_name=url.split('/')[-1])

                await message.delete_messages()

            except aiohttp.InvalidURL:
                await update.reply('**لینک ارسالی اشتباه است**')

        await client.run_until_disconnected()

asyncio.run(main())
