from flask import Flask, jsonify, json, request

with open('records.json') as f:
    all_records = json.load(f)

app = Flask(__name__)

@app.route('/records', methods=['GET'])
def get_all_records():
	return jsonify(all_records)

@app.route('/records', methods=['POST'])
def create_a_record():
    if not request.json or not 'name' in request.json:
        return jsonify({'error':'the new record needs to have a band name'}), 400
    new_record = {
            'name': request.json['name']
#            'albums': request.json['albums']
    }
    all_records.append(new_record)
    return jsonify({'message': 'created: /records/{}'.format(new_record['name'])}), 201

@app.route('/records/<bandname>', methods=['GET','DELETE'])
def get_albums_by_band(bandname):
    albums = [band['albums'] for band in all_records if band['name'] == bandname]
    if len(albums)==0:
        return jsonify({'error':'band name not found!'}), 404
    else:
        response = [album['title'] for album in albums[0]]
        return jsonify(response), 200

@app.route('/records/<bandname>', methods=['POST'])
def create_a_bandname(bandname):
    new_albums = [band for band in all_records if band['name'] == bandname]
    if len(new_albums)==0:
        return jsonify({'error':'band name not found!'}), 404
    new_albums_1 = {
            'name': request.json['name']
#            "albums": request.json['albums']
    }
    all_records.append(new_albums_1)
    return jsonify({'message': 'created: /records/bandname/{}'.format(new_bandname['name'])}), 201

@app.route('/records/<bandname>', methods=['DELETE'])
def delete_a_band(bandname):
    matching_records = [band for band in all_records if band['name'] == bandname]
    if len(matching_records)==0:
        return jsonify({'error':'band name not found!'}), 404
    all_records.remove(matching_records[0])
    return jsonify({'success': True})

@app.route('/records/<bandname>/<albumtitle>', methods=['GET'])
def get_songs_by_band_and_album(bandname, albumtitle):
    albums = [band['albums'] for band in all_records if band['name'] == bandname]
    if len(albums)==0:
        return jsonify({'error':'band name not found!'}), 404      
    else:
        songs = [album['songs'] for album in albums[0] if album['title'] == albumtitle]
        if len(songs)==0:
            return jsonify({'error':'album title not found!'}), 404
        else:
            return jsonify(songs[0]), 200
    

if __name__ == '__main__':
	app.run(host='0.0.0.0',port='80')
