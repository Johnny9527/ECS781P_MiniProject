from flask import Flask, render_template, request, jsonify
import json
import requests
# import requests_cache

# requests_cache.install_cache('crime_api_cache', backend='sqlite', expire_after=36000)
app = Flask(__name__)

# cats_url_template = 'https://http.cat/{status_code}'

@app.route('/')
def test():
    return "<h1>This is a test messages!!!</h1>"

@app.route('/getcat/', methods=['GET'])
def cat():
    cats_url_template = 'https://http.cat/{status_code}'
    # my_status = request.args.get('status_code', '200')
    my_status = '200'
    cats_url = cats_url_template.format(status_code = my_status)

    resp = requests.get(cats_url)

    if resp.ok:
        print(resp.json())
        return
    else:
        print(resp.reason)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
