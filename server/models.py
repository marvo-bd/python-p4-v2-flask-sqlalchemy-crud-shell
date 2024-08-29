from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return 'Welcome to the Pet API!'

@app.route('/pets', methods=['POST'])
def create_pet():
    data = request.json
    new_pet = Pet(name=data['name'], species=data['species'])
    db.session.add(new_pet)
    db.session.commit()
    return jsonify(new_pet.id), 201

@app.route('/pets', methods=['GET'])
def get_pets():
    pets = Pet.query.all()
    return jsonify([{'id': pet.id, 'name': pet.name, 'species': pet.species} for pet in pets])

if __name__ == '__main__':
    app.run(port=5555, debug=True)
