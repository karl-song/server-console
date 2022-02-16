# coding=utf-8

from flask import Flask

import config
import json
from console import nginx 

app = Flask(__name__)

# 根页面
@app.route("/")
def hello_world():
    return config.nginx_conf_dir

# nginx console
@app.route("/nginx/start")
def nginx_start():
    return json.dumps(nginx.start(),ensure_ascii=False)

@app.route("/nginx/status")
def nginx_status():
    return json.dumps(nginx.start(),ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True)