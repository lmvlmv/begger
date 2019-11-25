FROM python:3
RUN pip install pipenv
RUN git clone https://github.com/lmvlmv/begger.git
WORKDIR begger
RUN pipenv install
RUN pipenv install flower
ENTRYPOINT pipenv run celery flower -A beggarplay --port=${LISTEN_PORT}
