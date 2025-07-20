import logging
import datetime
import os

# Create logs directory if not exists
os.makedirs("logs", exist_ok=True)

# Unique log file name
log_filename = datetime.datetime.now().strftime("logs/game_log_%Y%m%d_%H%M%S.txt")

# Logging config
logging.basicConfig(
    level=logging.INFO,
    filename=log_filename,
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s"
)
