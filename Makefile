build:
	docker build  . --rm -t app
start:
	docker run --rm -it -e PORT_APP=8000 --name app -p 8000:8000 app

