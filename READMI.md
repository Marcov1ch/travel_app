# Приложение

Приложение интерактивной карты с галереей фото и достижениями.

# Установка

```bash
git clone https://github.com/Marcov1ch/travel_app.git
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

# Запуск
```bash
cd travel_app
python manage.py runserver
```

# Стек
## Frontend:
- React Native
- Type Script
- ...

## Backend
- Python
- Django (main app)
- FastAPI (микросервисы)

## Data Base
- PostgreSQL
- Redis

# Git branch
**main** - прод
**develop** - разработка (интеграция)
**feature** - разработка новых функций или исправление
**release** - подготовка к релизу
**hotfix** - для исправлений в main ветке

## Архитектура

```
travel_app/                      
├── backend/                     # Все бэкенд-сервисы
│   ├── travel_app/              # Основной Django-проект
│   │   ├── settings/
│   │   │   ├── base.py          # Общие настройки
│   │   │   ├── local.py         # Для разработки
│   │   │   └── production.py    # Для продакшена
│   │   ├── urls.py
│   │   └── asgi.py/wsgi.py
│   │
│   ├── trips/                   # Django-приложение
│   │   ├── migrations/
│   │   ├── api/
│   │   │   ├── v1/              # Версионирование API
│   │   │   │   ├── urls.py
│   │   │   │   └── views.py
│   │   │   └── serializers.py
│   │   └── services.py          # Бизнес-логика
│   │
│   └── ai_service/              # FastAPI-микросервис
│       ├── app/
│       │   ├── core/            # Общие модули
│       │   ├── models/          # Модели ИИ
│       │   └── routes/          # Эндпоинты
│       └── requirements.txt     # Отдельные зависимости
│
├── frontend/                    # Мобильное приложение
│   └── mobile/                  # React Native
│       ├── src/
│       │   ├── api/             # API-клиент
│       │   └── screens/         # Экраны приложения
│       └── App.tsx
│
├── infrastructure/              # Инфраструктура
│   ├── docker/
│   │   ├── django.Dockerfile
│   │   └── fastapi.Dockerfile
│   └── nginx.conf
│
├── .env
├── .gitignore
└── README.md
```