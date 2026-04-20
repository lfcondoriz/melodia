# 🎵 Melodia

> Plataforma de streaming de música · FastAPI · React Native · React

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![CI](https://github.com/lfcondoriz/melodia/actions/workflows/ci.yml/badge.svg)

## Descripción

Melodia es una plataforma de streaming de música que permite a los usuarios
escuchar sus canciones favoritas, crear listas de reproducción y descubrir
nueva música.

Proyecto desarrollado como práctica de conceptos del mundo laboral:
GitHub Flow, CI/CD, Docker, TDD y arquitectura de APIs REST.

---

## Stack tecnológico

| Capa | Tecnología |
|---|---|
| API | FastAPI (Python 3.12) |
| Base de datos | PostgreSQL 16 |
| ORM | SQLAlchemy 2.0 + Alembic |
| Autenticación | JWT (python-jose) |
| Containerización | Docker + Docker Compose |
| Linting | Ruff |
| Testing | Pytest + HTTPX |
| CI/CD | GitHub Actions |

---

## Estructura del proyecto

```
melodia/
├── backend/
│   ├── main.py              ← entry point FastAPI
│   ├── database.py          ← conexión PostgreSQL
│   ├── dependencies.py      ← auth y get_db reutilizables
│   ├── models.py            ← modelos SQLAlchemy
│   ├── schemas.py           ← schemas Pydantic
│   ├── routers/
│   │   └── auth.py          ← endpoints de autenticación
│   ├── migrations/          ← Alembic
│   │   └── versions/
│   ├── tests/
│   │   ├── conftest.py
│   │   └── test_auth.py
│   ├── Dockerfile
│   └── requirements.txt
├── .github/
│   └── workflows/
│       └── ci.yml           ← GitHub Actions
├── docker-compose.yml
└── .env.example
```

---

## Variables de entorno

Copiá `.env.example` como `.env` y completá los valores:

```bash
cp .env.example .env
```

```bash
APP_NAME=melodia
APP_ENV=development

POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
POSTGRES_HOST=db
POSTGRES_PORT=5432

SECRET_KEY=
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> ⚠️ Nunca subas el archivo `.env` al repositorio.

---

## Instalación y uso

### Levantar el proyecto

```bash
docker compose up --build
```

Las migraciones se aplican automáticamente al iniciar.

### Detener y limpiar

```bash
# Solo detener
docker compose down

# Detener y eliminar volúmenes (resetea la DB)
docker compose down -v
```

### Acceder a la documentación

```
http://localhost:8000/docs
```

---

## Endpoints disponibles

### Auth
| Método | Endpoint | Descripción | Auth |
|---|---|---|---|
| POST | `/auth/register` | Registro de usuario | ❌ |
| POST | `/auth/login` | Login, devuelve JWT | ❌ |
| GET | `/auth/me` | Usuario actual | ✅ |

### Sistema
| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/` | Bienvenida |
| GET | `/health` | Estado de la API y DB |

---

## Testing

```bash
# Correr todos los tests
docker compose exec api pytest

# Con detalle
docker compose exec api pytest -v

# Con cobertura
docker compose exec api pytest --cov=.
```

---

## Linting

```bash
# Verificar y corregir automáticamente
ruff check --fix backend/
ruff format backend/

# Solo verificar (sin cambios)
ruff check backend/
```

---

## Flujo de desarrollo (GitHub Flow)

Este proyecto simula trabajo en equipo usando GitHub Flow:

```
main              ← producción, siempre estable
└── feature/xxx   ← nueva funcionalidad
└── fix/xxx       ← corrección de bug
└── docs/xxx      ← documentación
```

**Reglas:**
- ❌ Nunca commitear directo a `main`
- ✅ Cada cambio = una rama = un Pull Request
- ✅ El PR solo se mergea si el CI está verde

---

## Roadmap

- [x] Setup del proyecto con Docker
- [x] CI/CD con GitHub Actions (ruff + pytest)
- [x] Conexión a PostgreSQL con SQLAlchemy
- [x] Migraciones con Alembic
- [x] Registro de usuarios
- [x] Login con JWT
- [x] Endpoint protegido `/auth/me`
- [ ] Login con Google (OAuth2)
- [ ] CRUD de canciones
- [ ] CRUD de playlists
- [ ] Frontend React Native
- [ ] Backoffice web con React
