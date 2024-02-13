from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# BOT_KEY = "6122956041:AAETM4_s2C-6mT2ek-X4GR6X9mfI3TOfqLg"    # TEST
GROUP_ID = -1002073052242                                     # TEST
GROUP_TITLE = "big092test"                                    # TEST
CHANNEL_ID = -1001513445928                                   # TEST
MONTENEGRO_THREAD_ID = 6                                      # TEST
SERBIA_THREAD_ID = 17                                         # TEST

BOT_KEY = "5626261222:AAHKJo2DzuU5vpMJuBQspVbPJmOge6nJaJs"  # PROD
# GROUP_ID = -1001763589351                                   # PROD
# GROUP_TITLE = "MonteMoveChat"                               # PROD
# CHANNEL_ID = -1001852241565                                 # PROD
# MONTENEGRO_THREAD_ID = 1                                    # PROD
# SERBIA_THREAD_ID = 11131                                    # PROD


storage = MemoryStorage()                                     # Test
# storage = RedisStorage(redis=redis)                         # Prod

bot = Bot(BOT_KEY)
dp = Dispatcher(storage=storage, bot=bot)
dp.middleware.setup(LoggingMiddleware())
DEV_KEY = {
    "chat": 0,
    "user": 0
}
