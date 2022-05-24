#! /usr/local/bin/python3
import cgi
import os
print("Content-Type: text/html")
print()
files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + \
        '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>WEB1</title>
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
        {listStr}
    </ol>
    <a href="create.py">create</a>
    <h2>{title}</h2>
    <p>{desc}</p>
</body>
</html>'''
      .format(title=pageId, desc=description, listStr=listStr))
