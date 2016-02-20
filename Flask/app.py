# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for

# Initialize the Flask application
app = Flask(__name__)
NOUN = "noun"
ADJECTIVE = "adjective"
VERB = "verb"

readFile = open("lib3.txt","r")
line = readFile.readline()
wordArray = line.split()
print(wordArray)
# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/hello/', methods=['POST'])
def hello():
<<<<<<< HEAD
=======

	readFile = open("/Users/FrankMAC/Desktop/Flask/lib3.txt")
	line = readFile.readline()
	stringArray = line[line.find(" "):].split()
	userKeyWordArray = (stringArray[0][1:-1]).split(",")
	print(stringArray)

>>>>>>> origin/master
	name=request.form['yourname']
	email=request.form['youremail']
	return render_template('form_action.html', name=name, email=email)

# Run the app :)
if __name__ == '__main__':
  app.run(
        host="127.0.0.1",
        port=int("5000"),
        debug=True
  )
