import os
import sys

from django.conf import settings




DEBUG = os.environ.get('DEBUG', 'on') == 'on'

#SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))
SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key }}')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return HttpResponse('Hello World')




@csrf_exempt
def post(request, *args):
    response = HttpResponse("Hello API Event Received")

    #parseHelloSignData(request, 'post_APP')


    return response


urlpatterns = (
    url(r'^$', index),
    url(r'^post', csrf_exempt(post))
)


application = get_wsgi_application()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
