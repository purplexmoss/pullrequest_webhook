from flask import json #read data from github
from flask import request
from flask import Flask

app = Flask(__name__) #this will be listening to HTTP

@app.route('/')
def api_root():
	return 'Wecome!'

@app.route('/github', methods=['POST']) #want to watch for githubposts
def api_gh_message():
	if request.headers['Content-Type'] == 'application/json':
		return json.dumps(request.json)

if __name__ == '__main__':
	app.run(debug=True)

