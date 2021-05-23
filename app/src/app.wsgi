import os
os.environ['DATABASE_URI'] = 'mysql://appsvc01:W3lcom344@db01/app'

import sys
sys.path.insert(0, '/var/www/app.oliverfletcher.io')

from app import app as application
