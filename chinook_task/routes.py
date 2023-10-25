def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('data_handler_with_value', '/{table}/{column}/{value}')
    config.add_route('data_handler_with_column', '/{table}/{column}')
    config.add_route('data_handler_with_table', '/{table}')
    config.add_route('test_db_connection', '/asd')

    
