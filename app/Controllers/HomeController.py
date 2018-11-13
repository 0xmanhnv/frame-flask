from flask import Blueprint, flash, render_template, request, session, abort, \
                  redirect, url_for
import os
from app import app
from app.Models import User


HomeController = Blueprint(
	'',
	__name__
)

@HomeController.route("/hello")
def hello():
	admin = User(username='admin', email='admin@example.com')
	return render_template('blog/home.html')