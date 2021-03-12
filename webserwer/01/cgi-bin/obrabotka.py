#!/usr/bin/ python3
import cgi

out_form = cgi.FieldStorage()

in_name = out_form.getfirst("in_name", "не задано")
in_comment = out_form.getfirst("in_comment", "не задано")

print("Content-type: text/html")
print()
print(in_name)
print(in_comment)