# coding=utf-8

import subprocess
import json
import config

def start():
    proc = subprocess.run("nginx -c"+config.nginx_conf, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout = proc.stdout.decode("gbk")
    stderr = proc.stderr.decode("gbk")

    return {
        'status':True if stderr=='' else False,
        'out':stdout,
        'err':stderr
    }

def status():
    proc = subprocess.run("netstat -anput | grep nginx", shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout = proc.stdout.decode("gbk")
    stderr = proc.stderr.decode("gbk")

    return {
        'status':True if stderr=='' else False,
        'out':stdout,
        'err':stderr
    }