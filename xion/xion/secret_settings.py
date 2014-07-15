# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : 'laptop_requests',
        'USER'     : 'field',
        'PASSWORD' : 'pro_bono',
        'HOST'     : '',
        #Uncomment when we are in production
        #'HOST'     : 'dbserve',
        'PORT'     : '',
    }
}


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_s3%4$7svj4u07-_7tvm^v)maj#0%y4g&2!ool!gp9^d*ipdh('