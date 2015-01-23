from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ba_usa.db'

class Bar(db.Model):
    __tablename__ = 'ba_states_new'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    address = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.String(2))
    rating = db.Column(db.Float(2))
    categories = db.Column(db.Text)
    lat = db.Column(db.Float(6))
    lon = db.Column(db.Float(6))

@app.route('/bars/', methods=['GET'])
def bars():
    if request.method == 'GET':
        results = Bar.query.limit(10).offset(0).all()

        json_results = []
        for result in results:
            d = {'id': result.id,
                 'name': result.name,
                 'address': result.address,
                 'city': result.city,
                 'state': result.state,
                 'rating': result.rating,
                 'categories': result.categories,
                 'lat': result.lat,
                 'lon': result.lon,}
            json_results.append(d)

    return jsonify(count=len(results), items=json_results)

@app.route('/bars/<state_abbr>', methods=['GET'])
def bars_state(state_abbr):
    if request.method == 'GET':
        results = Bar.query.filter_by(state=state_abbr).all()

        json_results = []
        for result in results:
            d = {'id': result.id,
                 'name': result.name,
                 'address': result.address,
                 'city': result.city,
                 'state': result.state,
                 'rating': result.rating,
                 'categories': result.categories,
                 'lat': result.lat,
                 'lon': result.lon,}
            json_results.append(d)

    return jsonify(count=len(results), items=json_results)

@app.route('/bars/<state_abbr>/<city_name>', methods=['GET'])
def bars_city(state_abbr, city_name):
    if request.method == 'GET':
        results = Bar.query.filter_by(state=state_abbr, city=city_name).all()
        city_name = city_name.replace('%20', ' ')

        json_results = []
        for result in results:
            d = {'id': result.id,
                 'name': result.name,
                 'address': result.address,
                 'city': result.city,
                 'state': result.state,
                 'rating': result.rating,
                 'categories': result.categories,
                 'lat': result.lat,
                 'lon': result.lon,}
            json_results.append(d)

    return jsonify(count=len(results), items=json_results)

@app.route('/bar/<int:bar_id>', methods=['GET'])
def bar(bar_id):
    if request.method == 'GET':
        result = Bar.query.filter_by(id=bar_id).first()

        d = {'name': result.name,
             'address': result.address,
             'city': result.city,
             'state': result.state,
             'rating': result.rating,
             'categories': result.categories,
             'lat': result.lat,
             'lon': result.lon,}

        return jsonify(items=d)

if __name__ == '__main__':
    app.run(debug=False)
