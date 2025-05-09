
build:
	docker buildx build -t my-flask-app . --load

run:
	docker run -p 18000:8000 my-flask-app