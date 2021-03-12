#!/usr/bin/ python3
import cgi
import html

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
text2 = form.getfirst("TEXT_2", "не задано")
text1 = html.escape(text1)
text2 = html.escape(text2)

out_form = cgi.FieldStorage()

in_name = out_form.getfirst("in_name", "не задано")
in_comment = out_form.getfirst("in_comment", "не задано")

print("Content-type: text/html")
print()
print(in_name)
print(in_comment)