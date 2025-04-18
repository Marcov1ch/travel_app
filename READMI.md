# Приложение

Приложение интерактивной карты с галереей фото и достижениями.

# Установка

```bash
git clone https://github.com/Marcov1ch/travel_app.git
cd travel_app

# Python
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

# Стек
## Frontend:
1.1 React Native
1.2 Type Script
1.3 ...

## Backend
2.1 Python
2.2 Django (main app)
2.3 FastAPI (микросервисы)

## Data Base
3.1 PostgreSQL
3.2 Redis

# Git branch
**main** - прод
**develop** - разработка (интеграция)
**feature** - разработка новых функций или исправление
**release** - подготовка к релизу
**hotfix** - для исправлений в main ветке

graph TD
    A[React Native] -->|HTTP API| B[Django]
    B -->|HTTP API| C[FastAPI]
    B --> D[(PostgreSQL)]
    C --> E[(Redis/Vector DB)]
