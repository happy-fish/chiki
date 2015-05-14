# coding: utf-8
__version__ = '1.0.0-dev'
__author__ = 'Linshao'
__email__ = '438985635@qq.com'

from flask import Flask
from flask_script import Manager

from .app import *
from .jinja import *
from .logger import *
from .media import *
from .uploads import *
from .verify import *
from .utils import *

manager = Manager(Flask(__name__))