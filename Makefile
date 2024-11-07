build:
	docker compose --env-file .env build

up:
	docker compose --env-file .env up -d

down:
	docker compose --env-file .env down

prune:
	docker compose --env-file .env down --rmi all -v --remove-orphans

shell:
	docker compose --env-file .env exec -it api /bin/sh
