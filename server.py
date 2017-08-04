from flask import Flask, request, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninja():
	return render_template('ninja.html')

@app.route('/ninja/<color>')
def ninja1(color):
	if color=="blue":
		turtle="leonardo"
	elif color=="orange":
		turtle="michelangelo"
	elif color=="red":
		turtle="raphael"
	elif color=="purple":
		turtle="donatello"
	else:
		turtle="notapril"
	return render_template('ninja1.html',hello=turtle)		

app.run(debug=True)