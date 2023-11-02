
FROM python:3.8
ARG VERSION_PLACEHOLDER

LABEL version=$VERSION_PLACEHOLDER
WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python3" , "app.py" ]
