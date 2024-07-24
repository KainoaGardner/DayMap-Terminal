import argparse
import os
from dotenv.main import load_dotenv

load_dotenv()

msg = "DayMap Daily Task Heatmap for Terminal"
parser = argparse.ArgumentParser(description=msg)

API_URL = os.getenv("API_URL")
AUTH_CACHE = os.getenv("AUTH_CACHE")

import app.main
