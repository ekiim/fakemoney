FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install pipenv 
RUN pipenv install --system --deploy --ignore-pipfile

WORKDIR /app/src
CMD ["python", "-m", "server"]
