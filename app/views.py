from app import app
from flask import render_template
import flask
from utils import utils

@app.route('/')
@app.route('/index')
def index():
    connection = "Connect"
    title = 'main'
    return render_template('index.html'
        ,title = title
        ,connection = connection
        ,cpu = True)

################################################
# API 
################################################

@app.route('/device')
def deviceAll():
    devices = utils.response("device", "all", False).generate()
    return flask.jsonify(devices)

@app.route('/device/<oid>')
def device(oid):
    devices = utils.response("device", oid, True).generate()
    return flask.jsonify(devices)

@app.route('/connection')
def connectionAll():
    cons = utils.response("connection", "all", True).generate()
    return flask.jsonify(cons)

@app.route('/connection/<oid>')
def connection(oid):
    cons = utils.response("connection", oid, True).generate()
    return flask.jsonify(cons)

@app.route('/site')
def siteAll():
    site = utils.response("site", "all", False).generate()
    return flask.jsonify(site)

@app.route('/site/<oid>')
def site(oid):
    site = utils.response("site", oid, True).generate()
    return flask.jsonify(site)

@app.route('/counter/<oid>')
def counter(oid):
    counter = utils.response("counter", oid, True).generate()
    return flask.jsonify(counter)