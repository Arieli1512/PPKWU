#!/usr/bin/env python3
from flask import Flask, request, jsonify
import re
import xmltodict
from dict2xml import dict2xml

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
def multipleCalc(num1 :int, num2: int, input : str):
    lowercase = len(re.findall(r'[a-z]', input))
    uppercase = len(re.findall(r'[A-Z]', input))
    digits = len(re.findall(r'[1-9]', input))
    rest = len(input) - lowercase - uppercase - digits
    return {
        "lowercase": lowercase,
        "uppercase": uppercase,
        "digits": digits,
        "special": rest,
        "sum": num1 + num2,
        "sub": num1 - num2,
        "mul": num1 * num2,
        "div": num1 // num2,
        "mod": num1 % num2      
    }

@app.route("/", methods=['POST'])
def get_numbers():
    request_xml = xmltodict.parse(request.get_data("root"))
    root = request_xml.get("root")
    if root is not None:
        request_xml= request_xml["root"]
        inputStr = request_xml.get("str")
        num1 = request_xml.get("num1")
        num2 = request_xml.get("num2")
        if num1 is not None and num2 is not None and inputStr is not None:
            output = multipleCalc(num1,num2,inputStr)
        else:
            if num1 is not None and num2 is not None:
                output = calculateInts(num1, num2)
            if inputStr is not None:
                output = stringStats(inputStr)
        return output


app.run(port=4080, host='0.0.0.0')