from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from tutorial.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'tutorial:static')
    config.add_route('home', '/')
    config.add_view(route_name='home', view='tutorial.views.my_view',
                    renderer='templates/mytemplate.pt')
    return config.make_wsgi_app()


