""" 
Them thu vien
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# khoi tao app 
static_url_path = ''
static_folder='../public'
template_folders = '../views'
app = Flask(__name__,
	static_folder=static_folder,
	static_url_path=static_url_path, 
	template_folder=template_folders
)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:18031997@localhost/python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
"""
controller
"""
from app.Controllers import HomeController
from app.Controllers import PageController
app.register_blueprint(HomeController)
app.register_blueprint(PageController)



"""
	xu ly loi 404
"""
# @app.errorhandler(404)
# def error404(error):
# 	return "404"