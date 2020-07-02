from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from flask_login import login_required, current_user, LoginManager
import requests as req

app = Flask(__name__)

db = SQLAlchemy(app)

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)

@app.route('/', methods=['GET'])
def index():
    print("Index")
    return render_template('login.html')

@app.route('/learn')
def learn():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))



@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'GET':
        return render_template('search.html')
    else:
        # return 'You searched ' + request.form['word']
        word = request.form['word']
        c = req.get('https://www.dictionary.com/browse/' + word)

        return render_template('display.html')


# @app.route('/learn', methods=['GET', 'POST'])
# @login_required
# def learn():
#     if request.method == 'GET':
#         if current_user.get_words_len() == 0:
#             return render_template('learn.html', base_msg='Add your first word to learn!')
#         return render_template('learn.html')
#     else:
#         return render_template('learn.html', )


def create_app():
    app.config['SECRET_KEY'] = 'wwzzxxsecretekeytodatabase'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Sri\\Documents\\UMKC\\Research\\OCEL\\flask_blog\\users.db'

    db.init_app(app)

    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    app_blueprint = Blueprint('app', __name__)
    app.register_blueprint(app_blueprint)
    return app



def run_app():
    app.config['SECRET_KEY'] = 'wwzzxxsecretekeytodatabase'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Sri\\Documents\\UMKC\\Research\\OCEL\\flask_blog\\users.db'

    db.init_app(app)

    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        print('in load user function')
        # print('User ID:', user_id)
        # since the user_id is just the primary key of our user table, use it in the query for the user
        from user import User
        return User.query.get(int(user_id))
    # app.config['SERVER_NAME'] = 'mg.dlearninglab.com'
    app.run(debug=True)


if __name__ == '__main__':
    run_app()