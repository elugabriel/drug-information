from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize Flask app
app = Flask(__name__)

# Set database connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drug_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define Drug model
class Drug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    class = db.Column(db.String(50), nullable=False)
    indications = db.Column(db.String(500), nullable=False)
    dosage = db.Column(db.String(200), nullable=False)
    side_effects = db.Column(db.String(500), nullable=False)

    def __init__(self, name, class, indications, dosage, side_effects):
        self.name = name
        self.class = class
        self.indications = indications
        self.dosage = dosage
        self.side_effects = side_effects

# Define Drug schema
class DrugSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'class', 'indications', 'dosage', 'side_effects')

# Initialize schema
drug_schema = DrugSchema()
drugs_schema = DrugSchema(many=True)

# Define route to add a new drug to the database
@app.route('/drugs', methods=['POST'])
def add_drug():
    name = request.json['name']
    class = request.json['class']
    indications = request.json['indications']
    dosage = request.json['dosage']
    side_effects = request.json['side_effects']

    new_drug = Drug(name, class, indications, dosage, side_effects)

    db.session.add(new_drug)
    db.session.commit()


