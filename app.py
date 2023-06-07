from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': ' Data Analyst',
  'location': ' Boston, MA',
  'salary': ' $100,000'
}, {
  'id': 2,
  'title': ' Frontend Engineer',
  'location': ' London, UK',
  'salary': ' $120,000'
}, {
  'id': 3,
  'title': ' Backend Engineer',
  'location': ' New York, US',
  'salary': ' $180,000'
}, {
  'id': 4,
  'title': ' Research Scientist',
  'location': ' San Francisco, USA',
  'salary': ' $200,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='DanJ')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
