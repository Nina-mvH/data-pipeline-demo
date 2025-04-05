from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from data_pipeline import Base, CaseDB


app = Flask(__name__)


DATABASE_URL = "mysql+pymysql://nvhoo:pass@localhost:3306/PPP_data"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

@app.route('/',methods=['GET','POST'])
def index():
    session = SessionLocal()
    query = session.query(CaseDB)
    results = []

    if request.method == 'POST':
        loan_number = request.form.get('loan_number')
        borrower_name = request.form.get('borrower_name')

        if loan_number:
            results = query.filter(CaseDB.loan_number == int(loan_number)).all()
        elif borrower_name:
            results = query.filter(CaseDB.borrower_name.like(f"%{borrower_name}%")).all()

    session.close()
    return render_template('index.html', results=results)

if __name__=="__main__":
    app.run(debug=True)
