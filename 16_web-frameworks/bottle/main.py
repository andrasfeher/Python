from bottle import route, run

@route('/')
def home():
    return "This is my home page"

run(host='localhost', port=9999)
