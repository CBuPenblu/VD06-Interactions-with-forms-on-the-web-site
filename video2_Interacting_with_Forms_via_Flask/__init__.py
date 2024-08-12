from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

from video2_Interacting_with_Forms_via_Flask import routes