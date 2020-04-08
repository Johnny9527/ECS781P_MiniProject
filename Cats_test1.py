from flask import Flask, render_template, request, jsonify
import json
import requests
import requests_cache

requests_cache.install_cache('crime_api_cache', backend='sqlite', expire_after=36000)
app = Flask(__name__)
crime_url_template = 'https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lng}&date={data}'
categories_url_template = 'https://data.police.uk/api/crime-categories?date={date}'

@app.route('/crimestat', methods=['GET'])
def crimechart():
    my_latitude = request.args.get('lat','51.52369')
    my_longitude = request.args.get('lng','-0.0395857')
    my_date = request.args.get('date','2018-11')
    crime_url = crime_url_template.format(lat = my_latitude, lng = my_longitude, data = my_date)
    resp = requests.get(crime_url)
    if resp.ok:
        return jsonify(resp.json())
    else:
        print(resp.reason)

@app.route('/allimages', methods=['GET'])
def get_all_images():
    random_cats_url = 'https://api.thecatapi.com/v1/images/search'
    resp = requests.get(random_cats_url)
    if resp.ok:
        return jsonify(resp.json())
    else:
        print(resp.reason)

@app.route('/getimages', methods=['GET'])
def get_images():
    specific_cats_url = 'https://api.thecatapi.com/v1/images/{image_id}'
    resp = requests.get(specific_cats_url)
    if resp.ok:
        return jsonify(resp.json())
    else:
        print(resp.reason)

if __name__=="__main__":
    app.run(host='0.0.0.0', port='80')
