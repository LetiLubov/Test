from flask import Flask, Response
import time

app = Flask(__name__)


# app.register_blueprint(sse, url_prefix='/streams')


@app.route('/')
def say_hello_world():
    return "Hello world!"


@app.route('/whoAmI')
def say_my_name():
    return Response("Liubov", mimetype="text")


@app.route('/time')
def what_is_time():
    def eventTime():
        while True:
            yield get_time() + '\n'

    return Response(eventTime(), mimetype="text/event")


def get_time():
    time.sleep(1)
    return time.ctime(time.time())


def bootapp():
    app.run(port=8080)
