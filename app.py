from flask import Flask, render_template

app = Flask(__name__)

def get_courses(id=None):

    courses = ['bb-block', 
               'bb-block i', 
               'bb-block ii', 
               'bb-block iii', 
               'makerlab i', 
               'makerlab ii', 
               'makerlab iii']
    
    if id is not None:
        return courses[int(id)]
    
    return courses


@app.route('/')
def hello_world():

    return render_template('index.html', data={'list_num': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

@app.route('/courses')
def courses():

    courses = get_courses()
    
    return render_template('courses.html', data={'courses': courses})

@app.route('/course/<id>')
def course(id):

    course = get_courses(id) 

    return render_template('course.html', data={'course': course})


app.run(debug=True)