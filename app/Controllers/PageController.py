from flask import Blueprint, flash, render_template, request, session, abort, \
                  redirect, url_for
import os
from app import app


PageController = Blueprint('page', __name__, url_prefix='/page')

@PageController.route("/hello")
def hello():
	return "page"