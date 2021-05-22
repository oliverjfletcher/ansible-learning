import os
os.environ['DATABASE_URI'] = 'mysql://app:app@db01/app'

import sys
sys.path.insert(0, '/var/www/app.oliverfletcher.io')

from app import app as application
