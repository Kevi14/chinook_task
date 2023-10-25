<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data</title>
</head>
<body>
    % if results and 'error' in results:
        <div class="error">
            ${results['error']}
        </div>
    % elif results:
        <table>
            <thead>
                <tr>
                    % for column in results[0].__table__.columns:
                        <th>${column.name}</th>
                    % endfor
                </tr>
            </thead>
            <tbody>
                % for row in results:
                    <tr>
                        % for column in row.__table__.columns:
                            <td>${getattr(row, column.name)}</td>
                        % endfor
                    </tr>
                % endfor
            </tbody>
        </table>
    % else:
        <div class="message">No data found.</div>
    % endif
</body>
</html>
