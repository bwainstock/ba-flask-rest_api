workers = 3
#pidfile = '/var/run/gunicorn/ba_flask_api.pid'
#daemon = True
errorlog = 'error.log'
accesslog = 'access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%({X-Real-IP}i)s"'
proc_name = 'gunicorn-ba_flask_api'
x_forwarded_for_header = "X-Real-IP"
