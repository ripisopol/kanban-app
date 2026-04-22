# kanban-app

A personal Kanban board built with FastAPI and SQLite.
Live at: kanban.rizalsolihin.my.id (coming soon)

## Stack
- Python 3.14
- FastAPI — REST API framework
- SQLAlchemy — ORM / database layer
- SQLite — local persistent storage
- HTML/CSS/JS — frontend, no framework

## Project Structure
kanban-app/
├── static/
│   └── index.html     # frontend
├── main.py            # API routes
├── models.py          # database models
├── database.py        # DB connection setup
└── requirements.txt   # Python dependencies

## API Routes
| Method | Route         | Description        |
|--------|---------------|--------------------|
| GET    | /health       | Server status      |
| GET    | /cards        | Get all cards      |
| POST   | /cards        | Create a card      |
| PATCH  | /cards/{id}   | Update/move a card |
| DELETE | /cards/{id}   | Delete a card      |

## Run Locally
# Clone the repo
git clone https://github.com/YOUR_USERNAME/kanban-app.git
cd kanban-app

# Create and activate venv
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run
uvicorn main:app --reload

# Visit
http://localhost:8000