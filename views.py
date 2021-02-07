from flask import Flask, redirect, request
from service.formater import PLAIN, get_formatted, SUPPORTED

#app must be initialized in the same directory than the views
app = Flask(__name__)

my_name = "Jose"
msg = "welcome to your first page!"

# Try in your browser to go to http://127.0.0.1:5000/
# Result: Jose welcome to your first page!
#
# Try: http://127.0.0.1:5000/?output=json
# Result: { "name":"Jose", "mgs":welcome to your first page!"}
@app.route('/')
def index():
    output = request.args.get('output')        # It gets an argument that you pass through the URL
    if not output:                             # To do that you need to use the keyword ?
        output = PLAIN                         # In this case the argument output can only have the values: plain, json, plain_uppercase, plain_lowercase
    return get_formatted(msg, my_name,
                         output.lower())

# http://127.0.0.1:5000/outputs
# plain, plain_uppercase, plain_lowercase, json
@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)

# http://127.0.0.1:5000/plain_uppercase
# JOSE WELCOME TO YOUR FIRST PAGE!
@app.route('/<output>')
def convert(output):
    return get_formatted(msg, my_name, output.lower())

# http://127.0.0.1:5000/jsonx2
# { "name":"Jose", "mgs":welcome to your first page!"}{ "name":"Jose", "mgs":welcome to your first page!"}
@app.route('/<output>x<int:n>')
def mult(output, n):
    return get_formatted(msg, my_name, output)*n

# http://127.0.0.1:5000/name=Lucas,msg=Welcome,output=plain_uppercase
# LUCAS WELCOME
@app.route('/name=<nme>,msg=<message>,output=<outp>')
def form(nme, message, outp):
    return get_formatted(message, nme, outp)