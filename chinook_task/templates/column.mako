<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Column Data</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }

        table, th, td {
            border: 1px solid black;
        }

        th, td {
            padding: 8px 12px;
        }
    </style>
</head>
<body>

<h2>Displaying data for column: ${column_name} in table: ${model.__tablename__}</h2>

% if 'error' in locals() and error:
    <div style="color: red;">
        ${error}
    </div>
% else:
    <table>
        <thead>
            <tr>
                <th>${column_name}</th>
            </tr>
        </thead>
        <tbody>
            % for row in data:
                <tr>
                    <td>${row[0]}</td>
                </tr>
            % endfor
        </tbody>
    </table>
% endif

</body>
</html>
