from AlumniConnect.settings.common import *

SECRET_KEY = "dikj)qxgkhe7v$y7l))d!!nkut&^6q7+x^@ys7c1z!#!&*94r5"

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# EMAIL SETTINGS
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Previous settings ...
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "<your_email_here>"
EMAIL_HOST_PASSWORD = "<your app password>"

# Custom setting. To email
# RECIPIENT_ADDRESS = 'rajanpatil2001@gmail.com'



DEFAULT_FROM_EMAIL = "Alumni Cell VJTI <vjtialumniconnect@gmail.com>"
BCC_EMAILS = ["rspatl_b19@it.vjti.ac.in"]

if DEBUG:
    STATICFILES_DIRS = (os.path.join(BASE_DIR, '..', 'static/'),)

    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    INTERNAL_IPS = ('127.0.0.1',)



# send_mail('A cool subject', 
        #   'A stunning message', 
        #   EMAIL_HOST_USER, 
        #   [RECIPIENT_ADDRESS])