migrate-taskfy:
	alembic upgrade head

start:
	uvicorn --host localhost --port 8000 main:app --reload

up-taskfy:
	docker compose -f docker-compose.yml up -d --build --force-recreate --remove-orphans

down-taskfy:
	docker compose -f docker-compose.yml down -v --remove-orphans