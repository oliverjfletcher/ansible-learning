activate_this = '/var/www/app/.venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
os.environ['DATABASE_URI'] = 'mysql://app:app@db01/app'

import sys
sys.path.insert(0, '/var/www/app')

from app import app as application

