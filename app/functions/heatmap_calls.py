import requests
import os
import json
import pandas as pd
from datetime import date

from app.other import TerminalColor, WEEKDAYS, MONTHS
from app import API_URL, AUTH_CACHE
from .auth import check_login, get_auth
