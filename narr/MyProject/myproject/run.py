from repoze.bfg.configuration import Configurator
from myproject.models import get_root

def app(global_config, **settings):
    """ This function returns a repoze.bfg.router.Router object.  It
    is usually called by the PasteDeploy framework during ``paster
    serve``"""
    zcml_file = settings.get('configure_zcml', 'configure.zcml')
    config = Configurator(root_factory=get_root, settings=settings,
                          zcml_file=zcml_file)
    return config.make_wsgi_app()


