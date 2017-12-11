from flask import Flask, render_template, request, make_response
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World - Chaitri'

@app.route('/authors')
def author_post_count():
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()

    count = 0
    strg = []
    for x in users:
        for y in posts:
            if y['userId'] == x['id']:
                count += 1
        strg.append(count)
        count = 0

    return render_template('author_count.html', data = zip(users,strg))

@app.route('/setcookie')
def set_cookie():
    resp = make_response(render_template('scookie.html'))
    resp.set_cookie('name',value="Chaitri")
    resp.set_cookie('age',value="21")
    return resp

@app.route('/getcookies')
def get_cookie():
    uname = request.cookies.get('name')
    uage = request.cookies.get('age')
    return render_template('gcookie.html',name=uname,age=uage)

@app.route('/robots.txt')
def deny_req():
    return render_template('deny.html')

@app.route('/html')
def ren_text():
    return render_template('text.html')

@app.route('/input', methods=['GET' , 'POST'])
def obtain_ip():
    if request.method == "POST":
        text = request.form['val']
        return render_template('showip.html', txt = text)
    else:
        return render_template('getip.html')

if __name__=="__main__":
    app.run()