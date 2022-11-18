FROM python:3.7.0

COPY ./blog /app/blog
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "blog.main:app", "--host=0.0.0.0", "--reload"]