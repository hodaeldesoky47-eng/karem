# SpaceXBio Makefile (no Docker)

.PHONY: help install backend frontend dev-backend dev-frontend test-backend test-frontend lint-frontend

help:
	@echo "Targets: install, backend, frontend, dev-backend, dev-frontend, test-backend, test-frontend"

install: backend frontend

backend:
	python -m pip install --upgrade pip
	pip install -r backend/requirements.txt

frontend:
	cd frontend && npm install --legacy-peer-deps

dev-backend:
	uvicorn backend.app.main:app --reload --port 8000

dev-frontend:
	cd frontend && npm run dev

test-backend:
	pytest -q

test-frontend:
	cd frontend && npm test -- --watchAll=false

lint-frontend:
	cd frontend && npm run lint --silent || true

