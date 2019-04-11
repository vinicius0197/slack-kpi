import os, json
from .handler import *

from flask import Flask, jsonify

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/kpi')
    def index_kpi():
        data = all_kpi()
        return jsonify(data)

    @app.route('/kpi/<int:id>')
    def show_kpi(id):
        return "kpi %d" % id

    @app.route('/kpi/statistics')
    def index_kpi_statistics():
        return "statistics"

    @app.route('/schedule/', methods=['GET', 'POST'])
    def index_job():
        return "jobs"

    def create_job():
        job_name = request.args.get(job_name)
        return job_name


    return app
