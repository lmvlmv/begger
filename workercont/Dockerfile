FROM python:3
RUN pip install pipenv
RUN git clone https://github.com/lmvlmv/begger.git
WORKDIR begger
RUN pipenv install
ENTRYPOINT [ "pipenv", "run", "celery", "-A", "beggarplay", "worker", "--concurrency=1"]
