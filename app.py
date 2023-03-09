from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title':'software developer'
  },
  {
    'id': 2,
    'title': 'testing'
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS,
                          company_name='hi')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

app.run(host='0.0.0.0', debug=True)