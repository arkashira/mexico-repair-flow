# Technical Specification – Mexico Repair Flow

---

## 1. Overview

**Mexico Repair Flow** is a lightweight Customer Information Management System (CIMS) designed to support repair shops in Mexico.  
It provides CRUD operations, search, and persistence to JSON. The system is intentionally minimal, yet fully testable, documented, and deployable as a Python library or a small REST API.

---

## 2. Architecture

```
┌─────────────────────┐
│   REST API Layer    │  (Optional – FastAPI)
└───────┬──────────────┘
        │
┌───────▼──────────────┐
│  Service Layer       │  (CustomerManager)
└───────┬──────────────┘
        │
┌───────▼──────────────┐
│  Repository Layer    │  (In‑Memory + JSON persistence)
└──────────────────────┘
```

* **REST API Layer** – Exposes endpoints for CRUD and search. Uses FastAPI for automatic docs and async support.  
* **Service Layer** – `CustomerManager` encapsulates business rules, validation, and orchestration.  
* **Repository Layer** – Abstracts data storage. Current implementation is in‑memory with optional JSON file persistence.

The design follows a **clean architecture** pattern: each layer depends only on the layer below it, enabling unit testing and future extensions (e.g., database adapters).

---

## 3. Components

| Layer | Component | Responsibility |
|-------|-----------|----------------|
| API | `api.py` | FastAPI router exposing endpoints. |
| Service | `customer_manager.py` | Business logic, validation, and orchestration. |
| Repository | `repository.py` | CRUD operations on `Customer` objects. |
| Model | `customer.py` | Data class representing a customer. |
| Persistence | `json_storage.py` | Load/Save JSON files. |
| Tests | `tests/` | Unit & integration tests. |

---

## 4. Data Model

```python
# customer.py
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Customer:
    id: int
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
```

* `id` – Auto‑incremented integer.  
* `email` – Must be unique and RFC‑5322 compliant.  
* `phone` & `address` – Optional.  
* Timestamps are ISO‑8601 strings.

---

## 5. Key APIs / Interfaces

### 5.1 Service Layer (`CustomerManager`)

| Method | Signature | Description |
|--------|-----------|-------------|
| `create_customer(name: str, email: str, phone: Optional[str] = None, address: Optional[str] = None) -> Customer` | Creates a new customer. Raises `ValueError` if email already exists. |
| `get_customer(customer_id: int) -> Customer` | Retrieves a customer by ID. Raises `KeyError` if not found. |
| `update_customer(customer_id: int, **kwargs) -> Customer` | Updates any mutable field. Raises `KeyError` if not found. |
| `search_customers(name: Optional[str] = None, email: Optional[str] = None) -> List[Customer]` | Returns list of customers matching filters. |
| `save_to_json(path: str) -> None` | Persists current state to JSON. |
| `load_from_json(path: str) -> None` | Loads state from JSON, replacing current data. |

### 5.2 REST API Endpoints (FastAPI)

| Path | Method | Body | Response | Notes |
|------|--------|------|----------|-------|
| `/customers/` | POST | `{"name": "...", "email": "...", ...}` | `201 Created` with `Customer` | Creates a customer. |
| `/customers/{id}` | GET | – | `200 OK` with `Customer` | Retrieve by ID. |
| `/customers/{id}` | PATCH | Partial fields | `200 OK` with updated `Customer` | Update. |
| `/customers/` | GET | `?name=&email=` | `200 OK` with list | Search. |
| `/customers/export/` | POST | `{"path": "file.json"}` | `200 OK` | Save to JSON. |
| `/customers/import/` | POST | `{"path": "file.json"}` | `200 OK` | Load from JSON. |

All endpoints return JSON and use Pydantic models for validation.

---

## 6. Technology Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| Language | Python 3.12 | Modern, type‑safe, and widely supported. |
| Web Framework | FastAPI | Async, auto‑docs, minimal boilerplate. |
| Data Validation | Pydantic | Built‑in with FastAPI, ensures schema correctness. |
| Testing | pytest + hypothesis | Unit tests + property‑based testing. |
| Packaging | Poetry | Dependency management, reproducible builds. |
| Linting | ruff | Fast, modern linting. |
| CI | GitHub Actions | Open‑source, integrates with Poetry. |

---

## 7. Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| fastapi | ^0.115.0 | Web framework |
| uvicorn | ^0.30.6 | ASGI server |
| pydantic | ^2.9.0 | Data validation |
| python-multipart | ^0.0.10 | File uploads (optional) |
| pytest | ^8.3.3 | Testing |
| hypothesis | ^6.108.0 | Property‑based tests |
| ruff | ^0.6.0 | Linting |
| poetry | ^1.8.4 | Dependency & packaging |

All dependencies are pinned to the latest minor releases at the time of writing.

---

## 8. Deployment

### 8.1 Local Development

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest

# Start API
poetry run uvicorn api:app --reload
```

### 8.2 Docker

```dockerfile
# Dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . .

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build & run:

```bash
docker build -t mexico-repair-flow .
docker run -p 8000:8000 mexico-repair-flow
```

### 8.3 Production Considerations

* **Database** – Replace `InMemoryRepository` with a SQLAlchemy or async‑pg adapter.  
* **Authentication** – Add OAuth2/JWT via FastAPI dependencies.  
* **Logging** – Use `structlog` or `loguru`.  
* **Monitoring** – Export Prometheus metrics.  
* **CI/CD** – GitHub Actions pipeline that runs tests, linting, builds Docker image, and pushes to registry.

---

## 9. Extensibility

| Feature | Current | Future |
|---------|---------|--------|
| Persistence | JSON file | PostgreSQL, MongoDB |
| Search | Linear scan | Full‑text search (Elasticsearch) |
| Validation | Basic | Schema‑driven, custom validators |
| API | REST | GraphQL, gRPC |
| UI | None | React/Vue SPA |

The modular design allows swapping out any component without touching the others.

---

## 10. Security & Compliance

* **Input Validation** – Pydantic ensures all fields meet type and format constraints.  
* **Email Uniqueness** – Enforced at service layer.  
* **Data Exposure** – API only exposes defined Pydantic models.  
* **JSON Storage** – Files are written with `utf-8` encoding; no sensitive data is logged.  
* **GDPR/Local Laws** – For production, add consent handling and data retention policies.

---

## 11. Testing Strategy

* **Unit Tests** – Test each method in isolation.  
* **Integration Tests** – Spin up FastAPI test client to hit endpoints.  
* **Property Tests** – Use Hypothesis to generate random customer data and validate invariants (e.g., email uniqueness).  
* **Coverage** – Target ≥ 90% line coverage.  
* **CI** – Run tests on every push and PR.

---

## 12. Documentation

* **Docstrings** – All public methods have comprehensive docstrings.  
* **OpenAPI** – FastAPI auto‑generates interactive docs at `/docs`.  
* **README** – Basic usage instructions (already provided).  
* **CHANGELOG** – Semantic versioning with changelog entries.

---

## 13. Release Process

1. Update `pyproject.toml` version.  
2. Commit changelog.  
3. Tag release: `git tag -a vX.Y.Z -m "Release X.Y.Z"`.  
4. Push tags: `git push --tags`.  
5. GitHub Actions builds and publishes Docker image to Docker Hub.  
6. Publish package to PyPI via Poetry.

---

## 14. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| In‑memory data loss | High | Add persistence layer early. |
| Email validation errors | Medium | Use robust regex and `email_validator` lib. |
| Concurrency issues | Medium | Use async locks or switch to DB. |
| JSON file corruption | Low | Validate schema on load; backup before overwrite. |

---

## 15. Appendix – Sample Code Snippets

```python
# api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from customer_manager import CustomerManager

app = FastAPI()
manager = CustomerManager()

class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str | None = None
    address: str | None = None

@app.post("/customers/", status_code=201, response_model=CustomerCreate)
def create_customer(dto: CustomerCreate):
    try:
        return manager.create_customer(**dto.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
```

```python
# repository.py
class InMemoryRepository:
    def __init__(self):
        self._data = {}
        self._next_id = 1

    def add(self, customer: Customer) -> Customer:
        customer.id = self._next_id
        self._data[self._next_id] = customer
        self._next_id += 1
        return customer
```

---

**End of Technical Specification**
