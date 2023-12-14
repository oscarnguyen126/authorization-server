run:
	gunicorn -w 4 -b 0.0.0.0 main:app

image:
	docker build -t api . && docker run -p 8000:8000 api
