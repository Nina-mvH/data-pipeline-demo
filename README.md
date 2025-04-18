# Overview
The provided code 1) reads in data from PPP FOIA csv files (downloadable at https://data.sba.gov/dataset/ppp-foia/resource/c1275a03-c25c-488a-bd95-403c4b2fa036?inner_span=True ) and uses a pydantic model to map the data to strongly types models. Then 2) the data is stored in a MySQL table (PPP_table) in the database PPP_data. This data can be explored using MySQL, or 3) the file UI.py can be used to run a local flask application allowing the data to be searched by loan_number or borrower_name. Results can be ordered alphabetically or by date_approved.

# How to Run Locally
In order to run this locally, you are going to need to download the following files: data_pipeline.py, make_table.sql, run,sh, UI.py, and templates/index.html. Once you have these files and a csv file, take the following steps to modify the code to your needs and run it. (The following steps were written for a Ubuntu 24.04.2 machine.)

*It's important to note that reading in one of the original csvs is time consuming; my virtual machine crashed when doing this, so I only used the top 10,000 lines from one of the csvs. If you're working with computational limitations, consider decreasing the size of the csv you're working with. Additionally, if you use a different csv than the one I did and run into a parsing error, it might be because I did not list that column data as optional and should be an easy fix.*

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
To create a MySQL Database, follow these steps:
- log into MySQL with your username and password, if you do not have a username or password you can make one
> sudo mysql
> CREATE USER 'yourusername'@'host' IDENTIFIED BY 'yourpassword';
- You should now be able to log in
> mysql --password
- Once you're logged into MySQL, create your database
> CREATE DATABASE databasename;
- Make sure you have all the privileges for this database
> GRANT ALL PRIVILEGES ON databasename.* TO 'yourusername'@'host';

## Make file edits as needed
These edits will likely include changing the name of the csv file you want to read and the database url. Currently, only a select few data columns are displayed in the flask web application, and you can also change what columns you want displayed. Consider changing the following:

### In make_table.sql
- update "PPP_table" to the name of your database table (lines 1, 2)

### In data_pipeline.py
- update "PPP_table" to the name of your database table (line 70)
- update "DATABASE_URL" to be "mysql+pymsql://*yourname*:*yourpassword*@localhost:3306/*yourdatabasename*" (line 127)
- update 'public_150k_plus_240930-small.csv' to the csv file name you want to read in (line 135)
- Note: 

### In run.sh
- change "PPP_data" to your database name
- update "./venv/bin/python3" depending on your use of a virtual environment or lack thereof

### In UI.py
- update "DATABASE_URL" to be "mysql+pymsql://*yourname*:*yourpassword*@localhost:3306/*yourdatabasename*" (line 11)

## Start Running
After you have all your packages ready and necessary file edits made, take the following steps in the terminal:
> ./run.sh //this will prompt you to enter your password...do that

At this point, your mySQL table should be populated and you can manually explore the data using SQL commands. If you want the simple UI...

> python UI.py //this will produce a link, open that link

This should open a web application that will allow you to search through the data.





