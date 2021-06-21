#from flask import Flask, redirect
import flask

application = flask.Flask(__name__)

@application.route('/')
def starting_url():
    return flask.redirect('https://www.tree-plenish.org/host-an-event')

if __name__ == '__main__':
    application.run()
