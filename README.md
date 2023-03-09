### 项目简介
    一个简单的docker-compose使用demo，可以快速部署一些常用的技术组件，也可以用来快速搭建一个微服务环境

### 目标
    快速部署一个微服务环境，基于consul和registrator实现服务的自动发现和注册，以及服务器节点的弹性扩容

### 组件
- nginx：网关、反向代理
- consul：服务发现和注册，并提供DNS服务
- registrator：容器运行监控，收集容器运行信息，实现服务的自动注册
- skywalking：链路追踪，用来对服务的运行状况进行分析

### 环境部署
    准备两台Linux主机，安装docker和docker-compose

    设置docker-compose环境变量: mv .env.example .env，修改.env

    修改微服务nginx配置：mv ./nginx/conf/pyserver.conf.example ./nginx/conf/pyserver.conf

    主机node1执行： docker-compose up -d consul-server pyserver registrator
    主机node2执行： docker-compose up -d consul-client pyserver registrator nginx

|主机名	| IP |	服务|
|  ----  | ----  |----  |
|node1   |192.168.1.130	|consul(server), pyserver(两个微服务:web1,web2), registrator|
|node2   |192.168.1.124 |consul(client), pyserver(两个微服务:web1,web2), registrator, nginx|

### 服务器节点扩容
方式一：基于upstream，可以通过upsync、consul-template等组件来实现upstream的动态变更

```
upstream pyserver{
    server 192.168.1.130:30003;
    server 192.168.1.124:30003;
}

server {
    listen 8080;
    server_name _;

    location / {
        proxy_pass http://pyserver;
    }

    error_log /var/log/nginx/pyserver1.log;
}
```

方式二：基于consul提供的DNS服务，来实现集群节点的弹性扩容

```
server {
    listen 8088;
    server_name _;

    resolver 127.0.0.1:8600;
    location / {
        set $service 'service_web1.service.consul';
        proxy_pass http://$service:30002;
    }

    error_log /var/log/nginx/pyserver2.log;
}
```