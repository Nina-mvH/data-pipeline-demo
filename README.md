###Overview
The provided code 1) reads in all the data from "public_150k_plus_240930-small.csv" and uses a pydantic model to map the data to strongly types models. Then 2) the data is stored in a MySQL table (PPP_table) in the database PPP_data. This data can be exlopred using MySQL, or 3) the file UI.py can be used to run a local flask application allowing the data to be searched by loan_number or borrower_name. Reuslts can be ordered alphabetically or by date_approved.

###How to Run Locally
In order to run this locally, you are going to need to download the following files: data_pipeline.py, make_table.sql, run,sh, UI.py, and templates/index.html. Once you have these files, take the following steps to modify the code to your needs and run it... 

## Download necessary packages:
The packages I have in my virtual environment include: 
- annotated-types   0.7.0
- blinker           1.9.0
- cffi              1.17.1
- click             8.1.8
- cryptography      44.0.2
- Flask             3.1.0
- Flask-SQLAlchemy  3.1.1
- greenlet          3.1.1
- itsdangerous      2.2.0
- Jinja2            3.1.6
- MarkupSafe        3.0.2
- mysql             0.0.3
- mysql-connector   2.2.9
- mysqlclient       2.2.7
- pip               24.0
- psycopg2          2.9.10
- psycopg2-binary   2.9.10
- pycparser         2.22
- pydantic          2.11.1
- pydantic_core     2.33.0
- PyMySQL           1.1.1
- SQLAlchemy        2.0.40
- typing_extensions 4.13.0
- typing-inspection 0.4.0
- Werkzeug          3.1.3

## Create a MySQL Database
do that

## Make file edits as needed
These edits will likely include changing the name of the csv file you want to read and the database url. Consider changing the following:

# In make_table.sql
- update "PPP_table" to the name of your database table (lines 1, 2)

# In data_pipeline.py
- update "PPP_table" to the name of your database table (line 70)
- update "DATABASE_URL" to be "mysql+pymsql://*yourname*:*yourpassword*@localhost:3306/*yourdatabasename*" (line 127)
- update 'public_150k_plus_240930-small.csv' to the csv file name you want to read in (line 135)

# In run.sh
- change "PPP_data" to your database name
- update "./venv/bin/python3" depending on your use of a virtual environment or lack thereof

# In UI.py
- update "DATABASE_URL" to be "mysql+pymsql://*yourname*:*yourpassword*@localhost:3306/*yourdatabasename*" (line 11)

## Start Running
After you have all your packages ready and necessary file edits made, take the following steps in the terminal:
>> ./run.sh //this will prompt you to enter your database password...do that
>> python UI.py //this will produce a link, open that to search and sort through the database





  



1. Look through the data for https://data.sba.gov/dataset/ppp-foia/resource/c1275a03-c25c-488a-bd95-403c4b2fa036?inner_span=True
2. Read it into a database of your choice that is able to run locally
3. Create a simple UI that is able to search through the data by ID or name
4. Bonus: If you can add sorting functionality based on alphabetical order or by date filed
5. Package this up into a codebase with a README that describes how to run this locally
6. Bonus: If you manage to figure out how to do this using Docker
7. Come back to us with any interesting insights you may have on the data
Graded on: Time to complete this, quality of your work, cleanliness of your code etc., insights you may have derived
8. Use Pydantic to map your data into strongly typed models that are used when reading data in
Use postgres

