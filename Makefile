DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env

APP_FILE = docker_compose\app.yml
STORAGES_FILE = docker_compose\storages.yml

DB_CONTAINER = db
APP_CONTAINER = main-app



.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up --build -d


.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER}

.PHONY: db-logs
db-logs:
	${LOGS} ${DB_CONTAINER}

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} down
