from logging import getLogger

from aiogram import Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from loader import CHANNEL_ID, GROUP_ID, GROUP_TITLE, MONTENEGRO_THREAD_ID, SERBIA_THREAD_ID, DEV_KEY, storage

logger = getLogger()


def register_transmitter_handlers(dp: Dispatcher):
    async def send_to_topic(msg: Message, post_url: str):
        lower = msg.text.lower() if msg.text else msg.caption.lower()
        if "#черногория" in lower:
            await msg.send_copy(
                GROUP_ID,
                message_thread_id=None,
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [InlineKeyboardButton(text="Посмотреть в канале", url=post_url)]
                    ]
                )
            )
        elif "#сербия" in lower:
            await msg.send_copy(
                GROUP_ID,
                message_thread_id=SERBIA_THREAD_ID,
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [InlineKeyboardButton(text="Посмотреть в канале", url=post_url)]
                    ]
                )
            )
        else:
            ...
        await storage.update_data(
            **DEV_KEY,
            data={
                "latest_msg_id": (await storage.get_data(**DEV_KEY))["latest_msg_id"]+1
            }
        )

    @dp.channel_post_handler(chat_id=CHANNEL_ID)
    async def new_post(post: Message):
        logger.info(f"New post {post.message_id}")
        new_msg_id = (await storage.get_data(**DEV_KEY))["latest_msg_id"]+1
        await send_to_topic(post, post.url)

        lower = post.text.lower() if post.text else post.caption.lower()
        if "#черногория" in lower:
            url=f"https://t.me/{GROUP_TITLE}/{MONTENEGRO_THREAD_ID}/{new_msg_id}"
        elif "#сербия" in lower:
            url = f"https://t.me/{GROUP_TITLE}/{SERBIA_THREAD_ID}/{new_msg_id}"
        else:
            url = f"https://t.me/{GROUP_TITLE}/{new_msg_id}"

        await post.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text="Комментировать",
                                             url=f"{url}")
                    ]
                ]
            )
        )
        logger.info(f"Copied!")

    @dp.message_handler(chat_id=GROUP_ID)
    async def new_msg(msg: Message):
        print(f"msg {msg.message_id} in {msg.message_thread_id}")
        await storage.update_data(
            **DEV_KEY,
            data={
                "latest_msg_id": msg.message_id
            }
        )
