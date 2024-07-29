import argparse
import os
from dotenv.main import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
AUTH_CACHE = os.getenv("AUTH_CACHE")

msg = "DayMap Daily Task Heatmap for Terminal"
parser = argparse.ArgumentParser(description=msg)

from app.parsers import users, heatmaps, entries

args = parser.parse_args()
from app.args_main import users_main, heatmaps_main, entires_main
