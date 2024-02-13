from aiogram.utils import executor

from admin_panel import register_admin_handlers
from handlers import register_user_handlers
from loader import dp
from statistics.stats_functions import scheduler
from transmitter import register_transmitter_handlers

register_user_handlers(dp)
register_admin_handlers(dp)
register_transmitter_handlers(dp)

scheduler.start()
executor.start_polling(dispatcher=dp, skip_updates=True)
