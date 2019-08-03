import logging

from flask import Flask, send_from_directory


app = Flask(__name__)


# Assets are retrieved directly from their parent folder.
@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('static/assets', path)

# Static files located in the root folder are retrieved directly from there, but their suffixes need to be
# mapped individually in order to avoid them from being hit by the most general (catch-all) rule.
@app.route('/<path:path>.css')
def send_css(path):
    return send_from_directory('static', f'{path}.css')

@app.route('/<path:path>.html')
def send_html(path):
    return send_from_directory('static', f'{path}.html')

@app.route('/<path:path>.ico')
def send_ico(path):
    return send_from_directory('static', f'{path}.ico')

@app.route('/<path:path>.js')
def send_js(path):
    return send_from_directory('static', f'{path}.js')

@app.route('/<path:path>.txt')
def send_txt(path):
    return send_from_directory('static', f'{path}.txt')

# Site root.
@app.route('/')
def site_root():
    return send_from_directory('static', 'index.html')

# Catch-all rule, responsible from handling Angular application routes (deeplinks).
@app.route('/<path:path>')
def angular_deeplinks(path):
    return send_from_directory('static', 'index.html')


# Internal server error handler.  
@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
