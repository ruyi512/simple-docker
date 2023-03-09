from flask import Flask
import sys
import os
from skywalking import agent, config

config.init(agent_collector_backend_services='192.168.1.130:11800', agent_protocol='grpc',
            agent_name='great-app-consumer-grpc',
            agent_instance_name='py_demo',
            agent_experimental_fork_support=True, agent_logging_level='DEBUG', agent_log_reporter_active=True,
            agent_meter_reporter_active=True,
            agent_profile_active=True)

agent.start()

app = Flask(__name__)


@app.route("/hello")
def hello():
    s = int(sys.argv[1])
    name = 'web1'
    if s == 30003:
        name = 'web2'
    ip = os.environ.get('HOST_IP', '')

    return 'hello ' + ip + ' service_' + name

@app.route("/")
def healthy():
    return 'ok'

if __name__ == '__main__':
    port = sys.argv[1]
    app.run(host='0.0.0.0', port=port)
