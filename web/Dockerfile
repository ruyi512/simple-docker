FROM python:3.7.4

ENV TZ Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN sed -i 's+http://deb.debian.org+http://mirrors.cloud.tencent.com+' /etc/apt/sources.list && \
  sed -i 's+http://security.debian.org+http://mirrors.cloud.tencent.com+' /etc/apt/sources.list

ADD ./workspace /app
WORKDIR /app

RUN apt-get update \
    && apt-get install -y supervisor \
    && pip install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*
