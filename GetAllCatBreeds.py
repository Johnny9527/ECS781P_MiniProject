import http.client
from flask import Flask

app = Flask(__name__)

@app.route('/getallcatbreeds', methods=['GET'])    # Method GET.
def test():
    conn = http.client.HTTPSConnection("api.thecatapi.com")
    headers = { 'x-api-key': "DEMO-API-KEY" }    # Call the API.

    conn.request("GET", "/v1/breeds?attach_breed=0", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")    # Use decode to change bytes into string.

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port='80')
