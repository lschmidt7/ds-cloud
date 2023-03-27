from flask import Flask

app = Flask(__name__)

@app.route("/home")
def index():
	return 'Olá Growdevers!'

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)