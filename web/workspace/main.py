from flask import Flask
import sys
import os
from skywalking import agent, config
import requests
from mysql_demo import test_mysql

ip = os.environ.get('HOST_IP', '127.0.0.1') # 当前主机IP
port = int(sys.argv[1])
name = 'web1'
if port == 30003:
    name = 'web2'

sw_oap = os.environ.get('SW_OAP_ADDRESS', '192.168.1.130:11800')
config.init(agent_collector_backend_services=sw_oap, agent_protocol='grpc',
            agent_name='service_{name}'.format(name=name),
            agent_instance_name='server_{ip}'.format(ip=ip),
            agent_experimental_fork_support=True,
            agent_logging_level='DEBUG',
            agent_log_reporter_active=True,
            agent_meter_reporter_active=True,
            agent_profile_active=True)

agent.start()

app = Flask(__name__)

@app.route("/hello")
def hello():
    return 'hello ' + ip + ' service_' + name + ';' + sw_oap

@app.route("/")
def healthy():
    return 'ok'

@app.route("/get")
def get():
    test_mysql()
    response = requests.get('https://www.87cq.com/api/game/newest')
    return response.content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
