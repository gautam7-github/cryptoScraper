from flask import Flask,jsonify,render_template
from threading import Thread
import data
app = Flask(__name__)
# to prevent keys from being sorted
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/crypto/top25/')
def get_data():
    return jsonify(data.getData())

def run():
  app.run(host='0.0.0.0',port=8080)

def main():  
    t = Thread(target=run)
    t.start()
if __name__ == "__main__":
    main()