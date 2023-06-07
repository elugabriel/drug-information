from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drug_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()

class Drug(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10000))
    indication = db.Column(db.String(10000))
    trans_indication = db.Column(db.String(10000))
    dose = db.Column(db.String(10000))
    trans_dose = db.Column(db.String(10000))
    size = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.trans_indication
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get_drug", methods=['GET', 'POST'])
def get_drug():
    sickness_info = request.form.get('sickness')
    size_info = request.form.get('size')
   

    if request.form['sickness'] != '' and  request.form['size'] != '':
        drug = Drug.query.with_entities(Drug.name, 
                                    Drug.indication,
                                    Drug.trans_indication,
                                    Drug.dose,
                                    Drug.trans_dose,
                                    Drug.size).filter_by(trans_indication= sickness_info, size= size_info).all()
        return render_template('index.html', drug = drug)
  
    if request.form['sickness'] != '' and  request.form['size'] == '':
        drug = Drug.query.with_entities(Drug.name, 
                                    Drug.indication,
                                    Drug.trans_indication,
                                    Drug.dose,
                                    Drug.trans_dose,
                                    Drug.size).filter_by(trans_indication= sickness_info).all()
        return render_template('index.html', drug = drug)
  
    if request.form['sickness'] == '' and  request.form['size'] == '':
         
        
        return render_template('no_info.html')
    
    if request.form['sickness'] == '' and  request.form['size'] != '':
         
        
        return render_template('no_info.html')
    
  
         
        
        return render_template('no_info.html')


if __name__ == '__main__':
    app.run(debug=True)
