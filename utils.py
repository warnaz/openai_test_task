import time
from functools import wraps
from config import MAX_RETRY, DELAY_RETRY
from loguru import logger


def helpers(retry_count, delay, error):
    logger.error(f"Ошибка: {error}. Осталось попыток: {retry_count}. Повтор через {delay} сек...")
    time.sleep(delay)


def retry_on_failure(retry_count=MAX_RETRY, delay=DELAY_RETRY):
    # Декоратор для повторных попыток в случае ошибки, а также задержки между попытками
    # Можно еще все ошибки обработать, рекомендованные командой OpenAI: https://help.openai.com/en/articles/6897213-openai-library-error-types-guidance 
    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            nonlocal retry_count
            while retry_count > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    helpers(retry_count, delay, e)
                    retry_count -= 1

            return "Превышено количество попыток или другая ошибка."
        return wrapper_retry
    return decorator_retry
