#! /usr/local/bin/python3
import cgi
print("Content-Type: text/html")
print()
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form.getvalue("id")
else:
    pageId = 'Welcome'
print('''<!DOCTYPE html>
<html lang="ko">
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
    <p>The World Wide Web (WWW), commonly known as the Web, is the world's dominant software platform. It is an information space where documents and other web resources can be accessed through the Internet using a web browser. The Web has changed people's lives immeasurably.It is the primary tool billions of people worldwide use to interact on the Internet.</p>
</body>
</html>'''
      .format(title=pageId))
