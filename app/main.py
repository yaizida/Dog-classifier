from fastapi import FastAPI

# Импортируем настройки проекта из config.py.
from core.config import settings

# Устанавливаем заголовок приложения при помощи аргумента title,
# в качестве значения указываем атрибут app_title объекта settings.
app = FastAPI(title=settings.app_title)
