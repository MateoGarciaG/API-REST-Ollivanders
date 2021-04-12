# Flask and Flask things
from flask import Flask, request, redirect, render_template, url_for, g, session
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, DataRequired, EqualTo, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Flask RESTful
from flask_restful import Resource, Api

# Importamos CORS
from flask_cors import CORS

# Import Resources
from resources.wellcome import Wellcome
from resources.inventario import Inventario
from resources.updateQuality import UpdateQuality
from resources.items import Items
from resources.quality import Quality
from resources.sellin import Sellin

# Import from Repository the db_connection.py
from repository import db_connection
# * iMPORT Get_db

# Import Users Model SQLAlchemy
from repository.models.users import User

app = Flask(__name__)
# secret key
app.secret_key = 'secretkey'

CORS(app)

if app.config["ENV"] == "production":
    # Configuration APP Flask Production
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "testing":
    # Configuration APP Flask Testing
    app.config.from_object("config.TestingConfig")
else:
    # Configuration APP Flask Development
    app.config.from_object("config.DevelopmentConfig")

# Init the Flask APP
db_connection.init_app(app)

# *****************************************
# * API SECTION

# API REST to be able to test
api = Api(app, catch_all_404s=True)

# Add Resources
# api.add_resource(Wellcome, '/')
api.add_resource(Inventario, '/inventory')
# GET item by name: '/items/name/<string:item_name>'
# POST, DELETE: '/items'
api.add_resource(Items, '/items/name/<string:item_name>', '/items', '/items/id/<int:id_item>/')
api.add_resource(Sellin, '/items/sellin/<int:item_sell_in>')
api.add_resource(Quality, '/items/quality/<int:item_quality>')
api.add_resource(UpdateQuality, '/update_quality')





# ***********************************************************************
# ***********************************************************************
# * lOGIN Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


#* Bootstrap
bootstrap = Bootstrap(app)


# ***********************************************************************
# * Get User
@login_manager.user_loader
def load_user(user_id):
    
    db_connection.get_db()
    
    return g.User.query.get(int(user_id))



# ***********************************************************************
# ***********************************************************************
# * lOGIN AND REGISTER FLASKFORM, FLASK-WTFORM
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('<h2>Remember me</h2>')


class RegisterForm(FlaskForm):
    # email = StringField(label='Email Address:',
    #                     validators=[Email(), DataRequired()])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])


# ***********************************************************************

# * BEFORE request
# ******************************************
@app.before_request
def before_request():
    
    db_connection.get_db()
    
    if 'user_id' in session:
        
        user = g.User.query.filter_by(username=session['user_id']).first()
        
    
    else:
        user = {"name": "Guest"}
    
    g.user_session = user


# * APP ROUTES
# ******************************************
# * RUOTE REDIRECCIONAR
@app.route('/')
def redireccionar():
    """
    RUTA REDIRECCIONAR A LA RUTA HOME
    """

    return redirect(url_for('home'))


# ******************************************

# ******************************************
# * RUOTE HOME
@app.route('/home')
def home():
    """
    RUTA home
    """

    return render_template('home.html')


# ******************************************

# ******************************************
# * RUOTE LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    RUTA LOGIN
    """
    
    db_connection.get_db()

    form = LoginForm()

    if form.validate_on_submit():
        
        # Eliminamos la anterior session
        session.pop('user_id', None)
        session['logged_in'] = False
        
        user = g.User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                
                #Creamos la session para el usuario actual
                session['user_id'] = user.id
                # Logged in = True
                session['logged_in'] = True
                
                return redirect(url_for('dashboard'))

        return '<h1>Invalid username or password</h1>'
        # return render_template('login.html', error_form='<h1>Invalid username or password</h1>')
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

    # return render_template('login.html')


# ******************************************
# ******************************************
# * RUOTE REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    RUTA REGISTER
    """

    db = db_connection.get_db()

    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = g.User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return render_template('register.html', form="", success=True)
        # return '<h1>New user has been created!</h1>'
        # return redirect(url_for('login'))
        # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('register.html', form=form)

    # return render_template('register.html')


# ******************************************
# ******************************************
# * ROUTE DashBoard

@app.route('/dashboard')
@login_required
def dashboard():
    
    if g.user_session == {"name": "Guest"}:
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', name=current_user.username, user_data=g.user_session)


# ******************************************
# * ROUTE LOGOUT
@app.route('/logout')
@login_required
def logout():
    session['logged_in'] = False
    logout_user()
    return redirect(url_for('home'))



# ******************************************
# ******************************************
# * IF MAIN

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
