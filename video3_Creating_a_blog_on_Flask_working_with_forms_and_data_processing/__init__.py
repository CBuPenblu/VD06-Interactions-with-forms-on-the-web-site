from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

from video3_Creating_a_blog_on_Flask_working_with_forms_and_data_processing import routes