import os
from flask import Flask

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'flask_base.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #bagels: a simple application
    @app.route('/bagels')
    def hello():
        return 'bagels game to come'

    return app


#cd into folder and type the following to run:
#$ export FLASK_APP=flask_base
#$ export FLASK_ENV=development
#$ flask run
