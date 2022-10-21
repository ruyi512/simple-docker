from flask import Flask
import sys
import os

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
