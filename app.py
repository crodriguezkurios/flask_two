from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world(request):
    name = request.args.get('name', 'World')
    
    return 'Hello, {}!'.format(name)

@app.route('/courses')
def courses():
    return 'Cursos'
