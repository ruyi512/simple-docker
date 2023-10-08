FROM openresty/openresty

ENV TZ Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN sed -i 's+http://deb.debian.org+http://mirrors.cloud.tencent.com+' /etc/apt/sources.list && \
  sed -i 's+http://security.debian.org+http://mirrors.cloud.tencent.com+' /etc/apt/sources.list

RUN apt-get update \
    && apt-get install -y wget \
    && wget https://mirrors.tuna.tsinghua.edu.cn/apache/skywalking/nginx-lua/0.6.0/skywalking-nginx-lua-0.6.0-src.tgz \
    && mkdir /usr/local/skywalking-nginx-lua \
    && tar -zxf skywalking-nginx-lua-0.6.0-src.tgz -C /usr/local/skywalking-nginx-lua