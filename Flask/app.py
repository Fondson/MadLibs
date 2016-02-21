# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
from random import randint

# Initialize the Flask application
app = Flask(__name__)
NOUN = "noun"
ADJECTIVE = "adjective"
VERB = "verb"

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
	global wordArray
	f = open("lib" + str(randint(1,3))+".txt","r")
	for line in f:
		wordArray = line.split(" ")
	numNouns = wordArray[0]
	numVerbs = wordArray[1]
	numAdjectives = wordArray[2]

	return render_template('form_submit.html', numNouns=numNouns, numVerbs=numVerbs, numAdjectives=numAdjectives)

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/hello/', methods=['POST'])
def hello():
	nounList=request.form['nouns'].split(',')
	verbList=request.form['verbs'].split(',')
	adjList=request.form['adjs'].split(',')
	for i in range(len(wordArray)-3):
		if wordArray[i+3]=='_n_':
			wordArray[i+3]= "-" + nounList.pop()
		elif wordArray[i+3]=='_v_':
			wordArray[i+3]= "-" + verbList.pop()
		elif wordArray[i+3]=='_a_':
			wordArray[i+3]= "-" + adjList.pop()

	string=''
	for i in range(len(wordArray)-3):
		string+=wordArray[i+3] + " "
	return render_template('form_action.html', string=string)

'''libs=[]	
@app.route('/test/')
def formm():
	
	f = open("lib3.txt","r")
	for line in f:
		wordArray = line.split(" ")
	
	for i in range(len(wordArray)):
		if (wordArray[i])[0]=='-':
			flag=False
			for j in range(len(libs)):
				if wordArray[i][1:]==libs[j]:
					flag=True
					break
			if not flag:
				libs.append(wordArray[i][1:])
	return render_template('form_submit_test.html', numnouns=libs[0], numverbs=libs[1], numadjectives=libs[2])
@app.route('/helloo/', methods=['POST'])
def helloo():
	inputList=[request.form['nouns'],request.form['verbs'],request.form['adjs']]
	for i in range(len(wordArray)):
		for j in range(len(libs)):
			if (wordArray[i])[1:]==libs[j]:
				wordArray[i]=inputList[j]
				break
	string=''
	for word in wordArray:
		string+=word + " "
	return render_template('form_action.html', string=string)
'''
# Run the app :)
if __name__ == '__main__':
  app.run(
        host="127.0.0.1",
        port=int("5000"),
        debug=True
  )