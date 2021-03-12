#!/usr/bin/ python3
# -*- coding: utf-8 -*-
import cgi
import html
import os
import http.cookies

print("Set-cookie: name=value")
out_form = cgi.FieldStorage()

in_name = out_form.getfirst("in_name", "не задано")
in_comment = out_form.getfirst("in_comment", "не задано")
#cookies
print("Content-type: text/html")
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")
if name is None:
    print("Set-cookie: name=value")
    print("Content-type: text/html\n")
    print("Cookies!!!")
else:
    print("Content-type: text/html\n")
    print("Cookies:")
    print(name.value)


print()
print(in_name)
print(in_comment)

