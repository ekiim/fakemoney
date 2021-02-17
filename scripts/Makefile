#
# Este archivo make es para la implementacion de docker,
#
# Para utilizarlo copielo al directorio raiz del proyecto.
#


.PHONY: clean test build install run stop restart terminal
DOCKER_IMAGE_NAME = fakemoney_docker
DOCKER_ID_FILE = .docker_id

clean:
	@echo "Cleaning Directory."
	find . -name __pycache__ -type d | xargs rm -rf
	rm ./src/server.log
	rm .docker_id

test:
	@echo "Running test suit."

build:
	@echo "Building Process."
	docker build -t $(DOCKER_IMAGE_NAME) .

install:
	@echo "Installing"
	
run:
	docker run -p 5000:5000 $(DOCKER_IMAGE_NAME) > $(DOCKER_ID_FILE)

stop:
	docker stop $$(cat $(DOCKER_ID_FILE))
	rm .docker_id

restart:
	docker restart $$(cat .docker_id)

terminal:
	docker run -it $(DOCKER_IMAGE_NAME) bash

