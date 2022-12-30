# Dockerfile for flask_resource.py

FROM python:3.9 as fr_dev
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=flask_resource.py
ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=5000
ENV FLASK_RUN_HOST=0.0.0.0
ENTRYPOINT [ "python" ]
CMD [ "flask_resource.py" ]
