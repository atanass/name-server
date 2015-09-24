#!/usr/bin/python
__author__ = 'atanasdichev'

from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    if request.args.get('name') == 'Icko':
        return Response("Go away, @#$@#%!!!!")
    else:
        return Response("Hello, %s!" % request.args.get('name', "World!"))



if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 4111, application)

