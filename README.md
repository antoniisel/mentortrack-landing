# MentorTrack — Landing

Лендинг продукта MentorTrack — SaaS для индивидуальных IT-менторов с AI-ассистентом.
Готовится к защите ДЗ-9 в рамках Product Studio (week 12).

## Стек

- Python 3.11 + Flask 3
- Jinja2 шаблоны (партиалы по блокам в `templates/partials/`)
- Tailwind CSS через CDN
- Alpine.js для интерактива (FAQ, форма, toggle тарифов)

## Локальный запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python app.py
```

Открыть `http://localhost:5000`.

## Деплой на Render (бесплатно)

1. Запушить репо на GitHub.
2. На [render.com](https://render.com) → New → Blueprint → подключить репо.
3. Render подхватит `render.yaml` автоматически.
4. Через 2–3 минуты получим публичный URL `https://mentortrack-landing.onrender.com`.

Free-tier «засыпает» через 15 мин неактивности — за 30 секунд до демо открой URL, чтобы прогреть.

## Структура

```
.
├── app.py                  # Flask: / и POST /api/lead
├── requirements.txt
├── render.yaml             # конфиг Render
├── plan.md                 # план лендинга
├── templates/
│   ├── base.html
│   ├── index.html
│   └── partials/           # 11 блоков лендинга
└── static/
    ├── css/custom.css
    └── js/main.js
```

## Команда

Селиванов А., Тарасов А., Манов М.
