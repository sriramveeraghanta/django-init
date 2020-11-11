from .common import *

APP_ENV = os.getenv('APP_ENV')

if APP_ENV == 'production':
    from .production import *
else:
    from .local import *