SASS_DIR = "./assets/scss"
CSS_DIR = "./static/css"

from flask import Flask, render_template


app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/<string:page_name>/')
def render_static(page_name):
    print(page_name)
    if page_name == "favicon.ico":
        return ""
    return render_template('index.html'.format(page_name))

if __name__ == '__main__':
    if app.debug:
        import sass
    sass.compile(dirname=(SASS_DIR, CSS_DIR))
    app.run()	
