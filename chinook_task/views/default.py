from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import aliased,sessionmaker

from ..models import (
    Artist,
    Album,
    Employee,
    Customer,
    Genre,
    Invoice,
    MediaType,
    Playlist,
    Track,
    PlaylistTrack,
    InvoiceLine
) 

table_map = {
    'Artist': Artist,
    'Album': Album,
    'Employee': Employee,
    'Customer': Customer,
    'Genre': Genre,
    'Invoice': Invoice,
    'MediaType': MediaType,
    'Playlist': Playlist,
    'Track': Track,
    'PlaylistTrack': PlaylistTrack,
    'InvoiceLine': InvoiceLine
}

@view_config(route_name='data_handler_with_value', renderer='chinook_task:templates/table_or_filter.mako')
@view_config(route_name='data_handler_with_table', renderer='chinook_task:templates/table_or_filter.mako')
def data_handler(request):
    error_message = ''
    results = None
    status = 200  # Default status (OK)

    try:
        table_name = request.matchdict.get('table')
        column_name = request.matchdict.get('column')
        filter_value = request.matchdict.get('value')

        if table_name not in table_map:
            raise ValueError('Invalid table name')

        model = table_map[table_name]
        Session = sessionmaker(bind=request.dbsession.bind)
        session = Session()

        if column_name and filter_value:
            results = session.query(model).filter_by(**{column_name: filter_value}).all()
        else:
            results = session.query(model).all()
    except Exception as e:
        error_message = str(e)
        status = 400  # Bad Request
        
    return {'results': results, 'error': error_message, 'status': status}

@view_config(route_name='data_handler_with_column', renderer='chinook_task:templates/column.mako')
def column_handler(request):
    error_message = ''
    results = None
    column_name = None
    model = None
    status = 200  # Default status (OK)
    try:
        table_name = request.matchdict.get('table')
        column_name = request.matchdict.get('column')

        if table_name not in table_map:
            raise ValueError('Invalid table name')

        model = table_map[table_name]
        Session = sessionmaker(bind=request.dbsession.bind)
        session = Session()

        results = session.query(getattr(model, column_name)).all()
    except AttributeError:
        error_message = 'Invalid column name'
        status = 400  # Bad Request
    except Exception as e:
        error_message = str(e)
        status = 400  # Bad Request
        
    return {
        'data': results,
        'column_name': column_name,
        'model': model,
        'error': error_message,
        'status': status
    }

@view_config(route_name='test_db_connection', renderer='json')
def test_db_connection(request):
    try:
        # Create a session
        Session = sessionmaker(bind=request.dbsession.bind)
        session = Session()

        # Test the connection by executing a simple query
        result = session.query(Artist).first()  # Replace with your actual query
    
        return {'message': 'Connection to the database successful!'}
    except SQLAlchemyError as e:
        return {'error': 'Error connecting to the database: {}'.format(str(e))}
    finally:
        session.close()

db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
