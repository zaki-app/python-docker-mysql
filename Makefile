build:
	docker-compose build

up:
	docker-compose up -d

ps:
	docker-compose ps

down:
	docker-compose down

db:
	docker-compose exec db bash

