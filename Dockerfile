FROM python:3.5.3

ENV FLASK_APP=app.py \
  GS_CREDENTIALS_JSON=/opt/secrets/creds.json

WORKDIR /opt/ebanolife/flask

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

VOLUME /opt/secrets

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
