start-dev:
  uvicorn app.main:app --reload

start:
  uvicorn app.main:app

up-taskfy:
	docker compose -f docker-compose.yml up -d --build --force-recreate --remove-orphans

down-taskfy:
	docker compose -f docker-compose.yml down -v --remove-orphans