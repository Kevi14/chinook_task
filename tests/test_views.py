import pytest
from pyramid import testing
from pyramid.testing import DummyRequest
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from unittest.mock import MagicMock, patch


@pytest.fixture
def dummy_request():
    request = DummyRequest()
    request.dbsession = MagicMock()
    request.dbsession.bind = 'some_bind'
    return request


@pytest.fixture
def dummy_sessionmaker():
    return MagicMock(spec=sessionmaker)


@pytest.fixture
def dummy_query():
    query = MagicMock()
    return query


@pytest.mark.parametrize("table,column,value", [
    ('Artist', 'Name', 'Queen'),
    ('Album', 'Title', 'Greatest Hits'),
])

def test_data_handler_with_value(dummy_request, dummy_sessionmaker, dummy_query, table, column, value):
    from chinook_task.views.default import data_handler

    dummy_request.matchdict = {'table': table, 'column': column, 'value': value}
    dummy_sessionmaker.return_value = dummy_query

    with patch('chinook_task.views.default.sessionmaker', return_value=dummy_sessionmaker):
        response = data_handler(dummy_request)

    assert 'results' in response
    assert 'error' in response
    assert response['status'] == 200  # Assuming the operation went smoothly


@pytest.mark.parametrize("table,column", [
    ('Artist', 'Name'),
    ('Album', 'Title'),
])
def test_data_handler_with_column(dummy_request, dummy_sessionmaker, dummy_query, table, column):
    from chinook_task.views.default import column_handler

    dummy_request.matchdict = {'table': table, 'column': column}
    dummy_sessionmaker.return_value = dummy_query

    with patch('chinook_task.views.default.sessionmaker', return_value=dummy_sessionmaker):
        response = column_handler(dummy_request)

    assert 'data' in response
    assert 'column_name' in response
    assert 'model' in response
    assert 'error' in response
    assert response['status'] == 200  # Assuming the operation went smoothly


@pytest.mark.parametrize("table", [
    'Artist',
    'Album',
])
def test_data_handler_with_table(dummy_request, dummy_sessionmaker, dummy_query, table):
    from chinook_task.views.default import data_handler

    dummy_request.matchdict = {'table': table}
    dummy_sessionmaker.return_value = dummy_query

    with patch('chinook_task.views.default.sessionmaker', return_value=dummy_sessionmaker):
        response = data_handler(dummy_request)

    assert 'results' in response
    assert 'error' in response
    assert response['status'] == 200  # Assuming the operation went smoothly




