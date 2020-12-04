FROM python:3.8.1
MAINTAINER mallycrip "migsking@naver.com"

COPY . .
WORKDIR .

RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=0
ENV GRPC_VERBOSITY=DEBUG
ENV GRPC_TRACE=http

ENTRYPOINT ["python"]
CMD ["run.py"]