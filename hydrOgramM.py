API_ID = 42  # Твои цифры без кавычек
API_ID = 42  # Твои цифры без кавычек
API_HASH = "42"  # В кавычках
API_HASH = "42"  # В кавычках
PHONE= "+42"
USER_ID= "42"

import asyncio
from hydrogram import Client, filters

# Хэндлер объявляем как обычную асинхронную функцию (без глобального декоратора)
async def hello(client, message):
    await message.reply("Hello from Hydrogram!")

async def main():
    # 1. Создаем клиент ИМЕННО ЗДЕСЬ, когда asyncio.run() уже создал event loop
    app = Client(
        "my_account",
        api_id=API_ID,
        api_hash=API_HASH,
    )
    
    # 2. Регистрируем хэндлер вручную через add_handler
    # (вместо @app.on_message)
    from hydrogram.handlers import MessageHandler
    app.add_handler(MessageHandler(hello, filters.private & ~filters.me))
    
    print("Запуск клиента Hydrogram...")
    # 3. Запускаем клиент в асинхронном контексте
    async with app:
        print("Клиент успешно запущен и слушает сообщения!")
        # Оставляем скрипт работать, пока не нажмут Ctrl+C
        while True:
            await asyncio.sleep(3600)

if __name__ == "__main__":
    try:
        # asyncio.run() гарантирует, что event loop будет создан ДО инициализации Client
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nБот остановлен.")
