from flask import Blueprint

app = Blueprint('views', __name__)

from . import auth,basic,errors,lesson
