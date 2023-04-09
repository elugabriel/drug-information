from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drug_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()

class Drug(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    sickness = db.Column(db.String(100))
    trans_sickness = db.Column(db.String(100))
    indication = db.Column(db.String(5000))
    trans_indication = db.Column(db.String(5000))
    size = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.trans_indication
    
@app.route('/')
def index():
    drug = Drug.query.with_entities(Drug.name, 
                                    Drug.sickness,
                                    Drug.trans_sickness,
                                    Drug.indication,
                                    Drug.trans_indication,
                                    Drug.size).all()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
