import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    filename="game_log.txt",
    datefmt='%Y-%m-%d %H:%M:%S'
)
