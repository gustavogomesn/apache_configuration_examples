import sys, os

sys.path.insert(0, os.path.dirname(__file__))

# Assuming that your main python files is called "main" and have the "app" class, like we have in Flask applications
from main import app as application