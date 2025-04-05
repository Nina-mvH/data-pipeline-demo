from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, asc, desc
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
    num_results = 0

    if request.method == 'POST':
        loan_number = request.form.get('loan_number')
        borrower_name = request.form.get('borrower_name')
        sort_by = request.form.get('sort_by')

        if loan_number:
            query = query.filter(CaseDB.loan_number == int(loan_number))
        elif borrower_name:
            query = query.filter(CaseDB.borrower_name.ilike(f"%{borrower_name}%"))

        if sort_by == 'name_asc':
            query = query.order_by(asc(CaseDB.borrower_name))
        elif sort_by == 'name_desc':
            query = query.order_by(desc(CaseDB.borrower_name))
        elif sort_by == 'date_asc':
            query = query.order_by(asc(CaseDB.date_approved))
        elif sort_by == 'date_desc':
            query = query.order_by(desc(CaseDB.date_approved))
        results = query.all()
        num_results = len(results)


    session.close()
    return render_template('index.html', results=results, num_results=num_results)

if __name__=="__main__":
    app.run(debug=True)
