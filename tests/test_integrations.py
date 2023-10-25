import pytest
from pyramid.paster import get_appsettings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from chinook_task import main
from webtest import TestApp

# Setup the application for integration tests
@pytest.fixture(scope='module')
def test_app():
    settings = get_appsettings('development.ini')
    app = main({}, **settings)
    return app

# Setup the test database
@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///Chinook_Sqlite_AutoIncrementPKs.sqlite')
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

@pytest.fixture(scope='module')
def test_web_app(test_app):
    return TestApp(test_app)

def test_data_handler_integration(test_web_app, test_db):
    response = test_web_app.get('/Artist/Name/Queen', status=200)

    # Asserting that the returned HTML contains the expected artist name
    assert "Queen" in response.text

    # Cleanup: Rollback the session to avoid changing the database state
    test_db.rollback()

# Test for invalid table name
def test_data_handler_invalid_table(test_web_app):
    # Status will be 200 even on error since mako is returning a response
    response = test_web_app.get('/NonExistentTable/Name/Value', status=200)
    assert 'No data found' in response.text

# Test for invalid column name
def test_data_handler_invalid_column(test_web_app):
    response = test_web_app.get('/Artist/NonExistentColumn/Value', status=200)
    assert 'Invalid column name' in response.text
