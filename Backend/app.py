from flask import Flask, request, jsonify,make_response
from flask_cors import CORS
from models import *
from flask_migrate import Migrate


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x2a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user=User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'success': False, 'message': 'Invalid username or password'}), 401
    if user.password==password:
        return jsonify({'success': True, 'message': 'Login successful'}), 200
    
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    user=User(
        username=username,
        password=password,
        email=email
    )
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Signup successful'})

@app.route('/api/breeds', methods=['GET'])
def get_breeds():
    breeds=Breeds.query.all()
    response=make_response([breed.to_dict()for breed in breeds],200)
    return response
    

@app.route('/api/breeds', methods=['POST'])
def create_breed():
    data = request.json
    name = data.get('name')
    speciality=data.get('speciality')
    image=data.get('image')

    breed=Breeds(
        name=name,
        speciality=speciality,
        image=image


    )
    db.session.add(breed)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Breed created successfully'})

@app.route('/api/Buys', methods=['GET'])
def get_Buys():
    Buys=Buy.query.all()
    response=make_response([Buy.to_dict()for Buy in Buys],200)
    return response
    

@app.route('/api/Buys', methods=['POST'])
def create_buy():
    data = request.json  # Assuming JSON data is sent via POST request
    name = data.get('name')
    email = data.get('email')
    address = data.get('address')
    contacts = data.get('contacts')
    

    # Create an instance of Buy and add to the database
    buy_instance = Buy(
        name=name,
        email=email,
        address=address,
        contacts=contacts,
        
    )
    db.session.add(buy_instance)
    db.session.commit()

    return jsonify({'message': 'Buy created successfully'})
@app.route('/api/activities', methods=['GET'])
def get_activities():
    activities=Activity.query.all()
    response=make_response([activity.to_dict()for activity in activities],200)
    return response



if __name__ == '__main__':
    app.run(port=5500, debug=True)