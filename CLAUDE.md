# MentorTrack landing — Product Studio, week 12

ДЗ-9 «Дизайн продукта»: продающий лендинг для защиты инвесторам.
Контекст продукта — в `context/`, требования ДЗ — в `week12hw.pdf`,
референсы стиля — `cyberroom.fortis.ru` и `locospadel.ru` (сохранены в `references/`).

## Итоги

- **Продакшн:** https://mentortrack-landing.onrender.com (Render free-tier, autodeploy на push)
- **Репо:** https://github.com/antoniisel/mentortrack-landing
- **План лендинга:** `plan.md` (структура, контент, обоснование решений, привязка к рубрике)

## Стек

Flask 3 · Jinja2 · Tailwind CDN · Alpine.js · gunicorn (на проде)

## Локальный запуск

```bash
source .venv/bin/activate
python app.py
# → http://localhost:5050
```

## Структура лендинга (11 логических блоков)

`nav → hero → pain → solution → mockups → how_it_works → audience → pricing → social_proof → faq → final_cta → footer`

Все партиалы — в `templates/partials/`. Главный шаблон — `templates/index.html`,
каркас (шрифты, Tailwind-конфиг, мета) — `templates/base.html`.

## Соответствие рубрике ДЗ-9 (10/10)

| Критерий | Балл | Где |
|---|---|---|
| ≥ 5 логических блоков | 3 | 11 блоков |
| Актуальный контент в каждом блоке | 3 | цифры из `context/HW_5_ProdStd.txt` |
| Блок макетов продукта | 2 | `partials/mockups.html` — 3 экрана: дашборд, AI-фидбек, AI-план |
| Цена + модель + decision-driving | 2 | `partials/pricing.html` — Starter 1490 / Pro 2990 / Team 7990, toggle мес/год (−20%), бейдж «Популярный», ROI-аргумент, trial без карты |

## Команда

Селиванов Антоний, Тарасов Артём, Манов Михаил
