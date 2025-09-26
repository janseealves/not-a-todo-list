# Not a Todo List 📋

A simple and elegant task management API built with FastAPI, featuring both web API endpoints and a CLI interface.

*Uma API simples e elegante para gerenciamento de tarefas construída com FastAPI, apresentando endpoints de API web e uma interface CLI.*

## 🚀 Features

- **RESTful API** with FastAPI
- **SQLite Database** with SQLAlchemy ORM
- **CRUD Operations** for task management
- **CLI Interface** with Typer and Rich *(Under Construction 🚧)* / *(Em Construção 🚧)*
- **Data Validation** with Pydantic schemas
- **Automatic Documentation** with FastAPI's built-in Swagger UI

## 📁 Project Structure

```
app/
├── main.py              # FastAPI application entry point
├── api/
│   └── endpoints.py     # API route definitions
├── cli/
│   └── main.py         # CLI application (Under Construction 🚧)
├── core/
│   ├── config.py       # Configuration settings
│   ├── database.py     # Database connection and session management
│   ├── models.py       # SQLAlchemy ORM models
│   └── schemas.py      # Pydantic data models
├── services/
│   └── crud.py         # Database operations
└── db/
    └── tasks.db        # SQLite database file
```

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd not-a-todo-list
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🚦 Usage

### Running the API Server

```bash
cd app
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

- **Swagger UI Documentation**: `http://localhost:8000/docs`
- **ReDoc Documentation**: `http://localhost:8000/redoc`

### Using the CLI

> ⚠️ **Under Construction / Em Construção** - The CLI is currently a basic prototype and is being actively developed.

```bash
cd app/cli
python main.py
```

**Planned features / Recursos planejados:**
- Task management commands
- Rich formatted output
- Integration with API endpoints

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Welcome message |
| `GET` | `/tasks` | Retrieve all tasks |
| `POST` | `/task` | Create a new task |
| `GET` | `/task/{id}` | Retrieve a specific task |
| `PUT` | `/task/{id}` | Update a task |
| `DELETE` | `/task/{id}` | Delete a task |

## 🔧 Dependencies

- **FastAPI** (0.116.2) - Modern web framework for APIs
- **SQLAlchemy** (2.0.43) - SQL toolkit and ORM
- **Pydantic** (2.11.9) - Data validation using Python type hints
- **Uvicorn** (0.35.0) - ASGI server implementation
- **Typer** (0.17.4) - CLI framework
- **Rich** (14.1.0) - Rich text and beautiful formatting