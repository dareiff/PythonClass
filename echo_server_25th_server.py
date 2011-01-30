from DocXMLRPCServer import DocXMLRPCServer
import datetime
import json

# Create server
server = DocXMLRPCServer(("localhost", 8000))

# Register a function
def echo(message):
    "Accepts a message parameter and returns it unchanged."
    return message
    
def time():
    "Returns the datetime.datetime.now() to the client. That's all."
    return datetime.datetime.now()

def add(numbers):
    "Returns the sum of two numbers, separated by a '+' delimiter."
    numbers = numbers.split('+')
    print numbers
    number1 = int(numbers[0])
    print number1
    number2 = int(numbers[1])
    print number2
    return number1 + number2

def google_utc_time():
    google_utc = json.load("http://json-time.appspot.com/time.json")
    print google_utc.dumps()
    return google_utc.datetime

server.register_function(echo)
server.register_function(add)
server.register_function(time)
server.register_function(google_utc_time)

# Run the server's main loop
server.serve_forever()

# DocXMLRPCServer classes automatically create and serve documentation to 
# browsers, visit http://localhost:8000/ to see it.
