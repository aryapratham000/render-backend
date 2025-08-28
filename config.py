# config.py
import os

PROJECTX_USERNAME = os.getenv("PROJECTX_USERNAME")
PROJECTX_API_KEY = os.getenv("PROJECTX_API_KEY")
PROJECTX_BASE_URL = os.getenv("PROJECTX_BASE_URL", "https://api.topstepx.com")
