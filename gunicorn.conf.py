# gunicorn.conf.py
workers = 1
threads = 2
timeout = 180
preload_app = False
max_requests = 50
max_requests_jitter = 5
keepalive = 5
loglevel = "warning"
bind = "0.0.0.0:$PORT"