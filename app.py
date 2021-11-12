from loader import bot


async def on_shutdown(dp):
    await bot.close()


admin_id=635986455
async def on_startup(dp):
    # Подождем пока запустится база данных...
    await bot.send_message(admin_id, "Я запущен!")

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
