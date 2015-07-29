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
    devices = utils.getConn().getDevice("all")
    return flask.jsonify(devices)

@app.route('/device/<oid>')
def device(oid):
    devices = utils.getConn().getDevice(oid)
    return flask.jsonify(devices)

@app.route('/connection')
def connectionAll():
    cons = utils.getConn().getConnection("all")
    return flask.jsonify(cons)

@app.route('/connection/<oid>')
def connection(oid):
    cons = utils.getConn().getConnection(oid)
    return flask.jsonify(cons)

@app.route('/site')
def siteAll():
    site = utils.getConn().getSite("all")
    return flask.jsonify(site)