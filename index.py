#! /usr/local/bin/python3
import cgi
print("Content-Type: text/html")
print()
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form.getvalue("id")
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WEB1</title>
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
        <li><a href="index.py?id=HTML">HTML</a></li>
        <li><a href="index.py?id=CSS">CSS</a></li>
        <li><a href="index.py?id=JavaScript">JavaScript</a></li>
    </ol>
    <h2>{title}</h2>
    <p>{desc}</p>
</body>
</html>'''
      .format(title=pageId, desc=description))
