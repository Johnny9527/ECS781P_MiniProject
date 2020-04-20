from flask import Flask, jsonify, json, request

# Cat list dataset.
all_cats = [
        {
                "name": "catlist",
                "categories": [
                        {
                                "title":"cat1",
                                "details":[
                                                {"breeds": []},
                                                {"id": "d46"},
                                                {"url": "https://cdn2.thecatapi.com/images/d46.jpg"},
                                                {"width": 1024},
                                                {"height": 1280}
                                ]
                        },

                        {
                                "title":"cat2",
                                "details":[
                                                {"breeds":[]},
                                                {"id":"akf"},
                                                {"url":"https://cdn2.thecatapi.com/images/akf.jpg"},
                                                {"width":3456},
                                                {"height":5184}
                                ]
                        },

                        {
                                "title":"cat3",
                                "details":[
                                                {"breeds":[]},
                                                {"id":"dqn"},
                                                {"url":"https://cdn2.thecatapi.com/images/dqn.jpg"},
                                                {"width":560},
                                                {"height":480}
                                ]
                        },

                        {
                                "title":"cat4",
                                "details":[
                                                {"breeds":[]},
                                                {"id":"dev"},
                                                {"url":"https://cdn2.thecatapi.com/images/dev.jpg"},
                                                {"width":960},
                                                {"height":720}
                                ]
                        },

                        {
                                "title":"cat5",
                                "details":[
                                                {"breeds":[]},
                                                {"id":"2dl"},
                                                {"url":"https://cdn2.thecatapi.com/images/2dl.jpg"},
                                                {"width":300},
                                                {"height":306}
                                ]
                        },

                        {
                                "title":"cat6",
                                "details":[
                                                {"breeds":[]},
                                                {"id":"bsm"},
                                                {"url":"https://cdn2.thecatapi.com/images/bsm.jpg"},
                                                {"width":601},
                                                {"height":900}
                                ]
                        },

                        {
                                "title":"cat7",
                                "details":[
                                                {"breeds":[]},
                                                {"id":"MTcxMzc5Mg"},
                                                {"url":"https://cdn2.thecatapi.com/images/MTcxMzc5Mg.jpg"},
                                                {"width":640},
                                                {"height":429}
                                ]
                        },

                        {
                                "title":"cat8",
                                "details":[
                                                {"breeds":[]},
                                                {"id":"3f2"},
                                                {"url":"https://cdn2.thecatapi.com/images/3f2.jpg"},
                                                {"width":500},
                                                {"height":333}
                                ]
                        },

                        {
                                "title":"cat9",
                                "details":[
                                                {"breeds":[]},
                                                {"id":"73u"},
                                                {"url":"https://cdn2.thecatapi.com/images/73u.jpg"},
                                                {"width":500},
                                                {"height":375}
                                ]
                        },

                        {
                                "title":"cat10",
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

@app.route('/catlist', methods=['GET'])    # Get all cat list.
def getcatlist():
    return jsonify(all_cats)

@app.route('/<name>/<title>', methods=['GET'])    # Get a specific cat details.
def get_catsdetails_by_name_and_title(name,title):
    categories = [AllCats['categories'] for AllCats in all_cats if AllCats['name'] == name]
    if len(categories)==0:
        return jsonify({'error':'404 not found!'}), 404
    else:
        details = [category['details'] for category in categories[0] if category['title'] == title]
        if len(details)==0:
            return jsonify({'error':'cat title not found!'}), 404
        else:
            return jsonify(details[0]), 200

@app.route('/addnewcat', methods=['POST'])    # Add a new cat to the list.
def add_new_cat():
    if not request.json or not 'name' in request.json:
        return jsonify({'error': 'A name is needed.'}), 400

    new_cat = {
        'name': request.json['name'],
        'categories': request.json.get('categories', ''),
        'breeds': request.json.get('breeds', ''),
        'id': request.json.get('id', ''),
        'url': request.json.get('url', ''),
        'width': request.json.get('width', ''),
        'height': request.json.get('height', '')
    }
    all_cats.append(new_cat)
    return jsonify({'message': 'created: /addnewcat/{}'.format(new_cat['name'])}), 201

@app.route('/catlist/<catname>', methods=['DELETE'])    # Delete a specific cat from the cat list.
def delete_a_catname(catname):
    matching_cats = [name for name in all_cats if name['name'] == catname]
    if len(matching_cats)==0:
        return jsonify({'error':'cat name not found!'}), 404
    all_cats.remove(matching_cats[0])
    return jsonify({'success': True})

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port='80')
