import pandas
import json 
from difflib import get_close_matches

data = json.load(open("data.json"))

def trans(value):
    value = value.lower()
    if value in data:
        return data[value]
    elif len(get_close_matches(value,data.keys())) > 0:
        answer = input( "Did you mean %s?(Y/n)\n" % get_close_matches(value,data)[0])
        if answer == 'Y':
            return data[get_close_matches(value,data)[0]]
    else:
        return "Error"

value = input("Enter a Word: ")
definition = trans(value)

if type(definition) == list:
    for item in definition:
        print(item)
else:
    print(definition)