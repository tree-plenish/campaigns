from flask import Flask, render_template
#import flask
import logging

application = Flask(__name__)
#application = flask.Flask(__name__)
#logging.basicConfig(filename="/var/log/web.stdout.log")
#logging.basicConfig(filename="/var/log/campaigns.log")

@application.route('/')
def starting_url():

    #campaign = flask.request.args.get("c")
    # print(campaign)
    #application.logger.info('Campaign Number: %s', campaign)
    return render_template('home.html')
    #return flask.redirect('https://www.tree-plenish.org/host-an-event')

if __name__ == '__main__':
    application.run()
