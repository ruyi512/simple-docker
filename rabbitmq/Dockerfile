FROM rabbitmq:3.8.11-management

ENV TZ Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN sed -i 's+http://deb.debian.org+http://mirrors.cloud.tencent.com+' /etc/apt/sources.list && \
  sed -i 's+http://security.debian.org+http://mirrors.cloud.tencent.com+' /etc/apt/sources.list

RUN apt-get update \
    && apt-get install -y rsync
