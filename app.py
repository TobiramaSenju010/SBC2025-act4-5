from flask import Flask, render_template,url_for, redirect
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)



@app.route('/')
def index():
    return render_template('users/index.html')

@app.route('/about')
def about():
    return render_template('users/about.html')

@app.route('/blog_details')
def blog_details():
    return render_template('users/blog_details.html')

@app.route('/blog_details2')
def blog_details2():
    return render_template('users/blog_details2.html')

@app.route('/blog_details3')
def blog_details3():
    return render_template('users/blog_details3.html')

@app.route('/blog_details4')
def blog_details4():
    return render_template('users/blog_details4.html')



if __name__ == '__main__':
    app.run(debug=True)