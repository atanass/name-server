#!/usr/bin/python
__author__ = 'atanasdichev'
import redis
import math
from werkzeug.wrappers import Request, Response

pool = redis.ConnectionPool(host='docker.neterra.skrill.net', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

@Request.application
def application(request):
    if request.method == "GET":
        return Response(r.get('attend'))
    elif request.method == "POST":
        r.incr('attend',amount=1)
        return Response('')
    else:
        return Response("Other")


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 4111, application)
