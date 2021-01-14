import os
import time
import sys
import logging
from subprocess import check_output
from flask import Flask, request
from flask import render_template


log = logging.getLogger('app')
app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    # say hello!
    log.info("Hello World!!")
    return render_template("index.html", vi=sys.version_info)


@app.route('/env')
def env():
    # dump all env variables
    return render_template("env.html", env=os.environ)

@app.route('/headers')
def request_headers():
    # dump all request headers
    return render_template("headers.html", headers=request.headers)

@app.route('/spawn')
def spawn(shell=False):
    # spawn and run an external process
    log.info("shell: {}", shell)
    output = check_output(['ps', 'auxf']).decode('utf8').split('\n')
    return render_template("spawn.html", output=output)


@app.route('/stdout')
def stdout():
    # write direct to STDOUT
    sys.stdout.write("Hello World!")
    sys.stdout.flush()
    return "Done"


@app.route('/stderr')
def stderr():
    # write direct to STDERR
    sys.stderr.write("Hello Error!")
    sys.stderr.flush()
    return "Done"


@app.route('/junk')
def junk():
    # Import code from PYTHONPATH included
    import junk
    return f"Junk: {junk.IM_HERE}"


@app.route('/longlog')
def long_log():
    # Generate a long log message
    length = int(request.args.get('length', 2048))
    chunks = int(length / 1024)
    for i in range(0, chunks):
        print('丂' * 1024, flush=True, end='')
    print('丂' * (length - 1024 * chunks), flush=True)
    return f'Wrote {length}'


@app.route('/413')
def return413():
    return ('Insert crazy 413 message here', 413)


@app.route('/sleep')
def sleep():
    # Force a slow response, wait for `time` seconds
    val = float(request.args.get('time', 1))
    time.sleep(val)
    return "Slept for {}\n".format(val)


@app.route('/exit')
def exit():
    # Force the app to crash
    sys.exit(0)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5001)))
