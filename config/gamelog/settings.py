import os

LOG_DIRS: str = "logs"
LOG_FILE_NAME: str = "game_log.log"

LOGS_FILE_PATH: str = os.path.join(LOG_DIRS, LOG_FILE_NAME)

if __name__ == "__main__":
    print(LOGS_FILE_PATH)
