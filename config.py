import os
import random
from dotenv import load_dotenv


load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY') # Ключ для работы с API OpenAI
PROXY = os.getenv('PROXY') # Прокси для работы OpenAI из РФ

MAX_RETRY = 3 # Количество попыток
DELAY_RETRY = random.randint(1, 5) # Задержка между попытками

