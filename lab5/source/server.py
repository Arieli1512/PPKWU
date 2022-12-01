#!/usr/bin/env python3
from flask import Flask, request, jsonify
import re

parameter_names = ["sum", "sub", "mul", "div", "mod"]

app = Flask(__name__)

def calculateInts(num1 :int, num2: int):
    return {"sum": num1 + num2, "sub": num1 - num2, "mul": num1 * num2, "div": num1 // num2, "mod": num1 % num2}
def stringStats(input : str):
    lowercase = len(re.findall(r'[a-z]', input))
    uppercase = len(re.findall(r'[A-Z]', input))
    digits = len(re.findall(r'[1-9]', input))
    rest = len(input) - lowercase - uppercase - digits
    return {
        "lowercase": lowercase,
        "uppercase": uppercase,
        "digits": digits,
        "special": rest
    }
@app.route("/", methods=['POST'])
def get_numbers():
    request_json = request.get_json()
    inputStr = request_json.get("str")
    num1 = request_json.get("num1")
    num2 = request_json.get("num2")
    if num1 is not None and num2 is not None:
        output = calculateInts(num1, num2)
    if inputStr is not None:
        output = stringStats(inputStr)
    return output


app.run(port=4080, host='0.0.0.0')