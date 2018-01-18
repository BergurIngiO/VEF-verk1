import os
from bottle import route, run

@route("/")
def index():
    return "<a href=/about> About</a>" "<a> </a>" "<a href=/bio> Biography</a>" "<a> </a>" "<a href=/pictures> Pictures</a>"
@route("/about")
def about():
    return "Hér eru upplýsngar um Steve Jobs"

@route("/bio")
def bio():
    return "Hér er biography frá Steve Jobs"

@route("/pictures")
def pictures():
    return "Hérna eru myndir frá lífi Steve Jobs"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
