from flask import Flask

app = Flask(__name__)

@app.route("/home")
def index():
	return 'Olá Growdevers!'

if __name__ == "__main__":
	app.run('0.0.0.0', debug=True)