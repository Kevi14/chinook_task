from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from .models.meta import Base 

def includeme(config):
    settings = config.get_settings()
    engine = engine_from_config(settings, 'sqlalchemy.')
    Base.metadata.bind = engine
    session_factory = sessionmaker(bind=engine)
    config.registry['db_session_factory'] = session_factory
    config.add_request_method(
        lambda r: session_factory(), 'db_session', reify=True
    )

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application. """
    with Configurator(settings=settings) as config:
        config.include('pyramid_mako')
        config.include('.routes')
        config.include('.models')
        includeme(config)
        config.scan()
    return config.make_wsgi_app()
