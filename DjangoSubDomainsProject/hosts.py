from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns("",
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'app1', 'App1.urls', name='app1'),
    host(r'app2', 'App2.urls', name='app2'),
)
