#!/usr/bin/env python

import os, json , cgi

print "Content-type: text/html"
print "Location: http://google.ca"
print
print """<html><body>
<style type=text/css>

h1{

text-align:center


}
</style>
<h1>I H3ARD u leik Mudkeipz</h1>

<form method=POST>
<input name=x>
</form>

<h3>"""

form = cgi.FieldStorage()

print "x was:  " + cgi.escape(str(form.getvalue('x')))

print """</h3></body></html>"""
