FROM python:3.12-slim


# Устанавливаем Python зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Создаем рабочую директорию
WORKDIR /app

# Копируем приложение
COPY . .

# Создаем директории для статики и медиа

# Устанавливаем права
RUN chmod +x manage.py

# Собираем статические файлы
