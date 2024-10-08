# URL Shortener

## Описание проекта

Этот проект представляет собой простой URL-укоротитель, который позволяет сокращать длинные ссылки до более короткого и удобного для использования формата. Основная функциональность включает создание сокращенных URL и их последующую обработку.

## Структура проекта

- `main.py` — основной файл, который содержит точку входа в программу и логику обработки запросов.
- `messages.py` — содержит текстовые сообщения и константы, которые используются в проекте.
- `regex_rules.py` — содержит регулярные выражения, которые применяются для проверки URL и других строковых данных.
- `utils/` — вспомогательная директория, содержащая модули:
  - `storage.py` — отвечает за сохранение и загрузку данных.
  - `url_request.py` — модуль для обработки запросов, связанных с URL.

## Установка

1. Клонируйте репозиторий или загрузите архив с кодом.
2. Убедитесь, что у вас установлен Python 3.x.
3. Установите необходимые зависимости (если они есть):
   ```bash
   pip install -r requirements.txt

## Запустите приложение

  bash
  
    python main.py
