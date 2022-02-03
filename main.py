import flask
import os

app = flask.Flask(__name__)
Shows = ['GOT', 'Patriot', 'Ozarks', 'South Park', 'True Detective']


@app.route("/")  # Python decorator
def main():
    return flask.render_template("index.html", len = len(Shows), Shows = Shows)

app.run(
    
    #host=os.getenv('IP', '0.0.0.0'),
    #port=int(os.getenv('PORT', 8080)),
    debug=True
)