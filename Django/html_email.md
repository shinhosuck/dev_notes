```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table style="padding: 1rem">
        <tr>
            <th style="text-align: start; font-size: 1.5rem;">
                MySite Blog
            </th>
        </tr>
        <tr>
            <td style="padding: 1rem 0; font-size: 1.2rem; max-width: 400px;">
                <span style="font-weight: bold; font-size: 1.2rem;">{{ name }}</span> recommend you to read "{{ post_title }}"!
            </td>
        </tr>
        <tr>
            <td style="padding: 1rem 0; max-width: 400px; font-size: 1.2rem;">
                <p>
                    Read "{{ post_title }}" at {{ post_url }}.
                </p>
            </td>
        </tr>
        <tr>
            <td style="padding: 1rem 0; max-width: 400px; font-size: 1.2rem;">
                <p>
                    Comment: {{ comments }}
                </p>
            </td>
        </tr>
    </table>
</body>
</html>
```
