from flask import Flask, abort, request
import json

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def parse_json():
    try:
        clipped_string = request.json['clipped_string']
    except:
        print('Invalid, please try another POST request key')
        abort(400)
    result_string = string_output(clipped_string)
    return_json = {
        "return_string": result_string,
    }
    return json.dumps(return_json)

def string_output(string):
    i = 0
    clipped_list = []
    for char in string:
        i += 1
        if i == 3:
            clipped_list.append(char)
            i = 0
    return "".join(clipped_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
