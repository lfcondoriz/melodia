# Melody

Music streaming platform developed as a software engineering project.

## Setup

### Prerequisites
- Python 3.11+
- pip

### Installation

1. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the development server:
```bash
uvicorn app.main:app --reload
```

The app will be available at `http://127.0.0.1:8000`

**Interactive API docs:** `http://127.0.0.1:8000/docs`

## Running Tests

```bash
pytest tests/ -v
```

## Documentation
- `docs/product/01-product-vision.md`
- `docs/adr/ADR-001-initial-architecture.md`

## Current Status
Project documentation database under development.