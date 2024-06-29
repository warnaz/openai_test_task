import httpx

from openai import OpenAI
from flask import Flask

from config import OPENAI_KEY, PROXY


# Настройки Flask
app = Flask(__name__)

# Настройки OpenAI
_http_client = httpx.Client(proxy=PROXY) # Кастомный клиент для работы с API OpenAI
openai = OpenAI(api_key=OPENAI_KEY, http_client=_http_client) # Настройки OpenAI
