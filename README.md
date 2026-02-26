# Faltmate

A flatmate app for listing and browsing apartments with chore management, expense splitting, calendars, and messaging.

## Features
- Flat owners can list their flats
- Users can browse available flats
- Chore/task management with rotating chores
- Expense splitting and bill tracking
- Calendar and event coordination
- Grocery list management
- Chat and messaging between flatmates

## Tech Stack
- **Backend**: Django + Django REST Framework
- **Frontend**: React
- **Task Queue**: Celery
- **Cache/Message Broker**: Redis
- **Database**: PostgreSQL

## Project Structure
```
faltmate/
├── backend/          # Django application
├── frontend/         # React application
├── docker-compose.yml
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 16+
- Docker & Docker Compose

### Installation

#### Backend
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### Frontend
```bash
cd frontend
npm install
npm start
```

#### Redis & Celery
```bash
docker-compose up
```

## License
MIT
