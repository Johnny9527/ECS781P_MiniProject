from flask import Flask, jsonify, json, request

all_cats = [
	{
		"name": "AllCats",
		"categories": [
			{
				"title":"Cat1",
				"details":[
						{"breeds": []},
						{"id": "d46"},
						{"url": "https://cdn2.thecatapi.com/images/d46.jpg"},
						{"width": 1024},
						{"height": 1280}
				]
			},
			
			{
				"title":"Cat2",
				"details":[
						{"breeds":[]},
						{"id":"akf"},
						{"url":"https://cdn2.thecatapi.com/images/akf.jpg"},
						{"width":3456},
						{"height":5184}
				]
			},
			
			{
				"title":"Cat3",
				"details":[
						{"breeds":[]},
						{"id":"dqn"},
						{"url":"https://cdn2.thecatapi.com/images/dqn.jpg"},
						{"width":560},
						{"height":480}
				]
			},
			
			{
				"title":"Cat4",
				"details":[
						{"breeds":[]},
						{"id":"dev"},
						{"url":"https://cdn2.thecatapi.com/images/dev.jpg"},
						{"width":960},
						{"height":720}
				]
			},
			
			{
				"title":"Cat5",
				"details":[
						{"breeds":[]},
						{"id":"2dl"},
						{"url":"https://cdn2.thecatapi.com/images/2dl.jpg"},
						{"width":300},
						{"height":306}
				]
			},
			
			{
				"title":"Cat6",
				"details":[
						{"breeds":[]},
						{"id":"bsm"},
						{"url":"https://cdn2.thecatapi.com/images/bsm.jpg"},
						{"width":601},
						{"height":900}
				]
			},
			
			{
				"title":"Cat7",
				"details":[
						{"breeds":[]},
						{"id":"MTcxMzc5Mg"},
						{"url":"https://cdn2.thecatapi.com/images/MTcxMzc5Mg.jpg"},
						{"width":640},
						{"height":429}
				]
			},
			
			{
				"title":"Cat8",
				"details":[
						{"breeds":[]},
						{"id":"3f2"},
						{"url":"https://cdn2.thecatapi.com/images/3f2.jpg"},
						{"width":500},
						{"height":333}
				]
			},
			
			{
				"title":"Cat9",
				"details":[
						{"breeds":[]},
						{"id":"73u"},
						{"url":"https://cdn2.thecatapi.com/images/73u.jpg"},
						{"width":500},
						{"height":375}
				]
			},
			
			{
				"title":"Cat10",
				"details":[
						{"breeds":[]},
						{"id":"bts"},
						{"url":"https://cdn2.thecatapi.com/images/bts.jpg"},
						{"width":640},
						{"height":480}
				]
			}
                ]
	}
]

app = Flask(__name__)

@app.route('/gettest', methods=['GET'])
def gettest():
    return jsonify(all_cats)

@app.route('/gettest/<name>', methods=['GET','DELETE'])
def get_albums_by_band(name):
    categories = [band['categories'] for band in all_cats if band['name'] == name]
    if len(categories)==0:
        return jsonify({'error':'band name not found!'}), 404
    else:
        response = [album['title'] for album in categories[0]]
        return jsonify(response), 200

@app.route('/gettest/<name>/<title>', methods=['GET'])
def get_songs_by_band_and_album(name, title):
    categories = [band['categories'] for band in all_cats if band['name'] == name]
    if len(categories)==0:
        return jsonify({'error':'band name not found!'}), 404
    else:
        details = [album['details'] for album in categories[0] if album['title'] == title]
        if len(details)==0:
            return jsonify({'error':'album title not found!'}), 404
        else:
            return jsonify(details[0]), 200

#@app.route('/posttest', methods=['GET', 'POST'])
#def posttest():
#    if request.method == 'POST': 
#        all_cats.append(request.values['catname'])
#        return 'New cat name is ' + request.values['catname'] 

#    return "<form method='post' action='/posttest'><input type='text' name='catname' />" \
#            "</br>" \
#           "<button type='submit'>Add New Cat</button></form>"

@app.route('/posttest', methods=['POST'])
def posttest():
    if not request.json or not 'name' in request.json:
        return jsonify({'error': 'A name is needed.'}), 400

    new_cat = {
        'name': request.json['name']
#        'categories': request.json.get('categories', '')
#        'cat': request.json['cat']
    }
    all_cats.append(new_cat)
    return jsonify({'message': 'created: /posttest/{}'.format(new_cat['name'])}), 201

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port='80')
