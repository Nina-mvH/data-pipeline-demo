
## Packages Used:
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
MarkupSafe        3.0.2
mysql             0.0.3
mysql-connector   2.2.9
mysqlclient       2.2.7
pip               24.0
psycopg2          2.9.10
psycopg2-binary   2.9.10
pycparser         2.22
pydantic          2.11.1
pydantic_core     2.33.0
PyMySQL           1.1.1
SQLAlchemy        2.0.40
typing_extensions 4.13.0
typing-inspection 0.4.0
Werkzeug          3.1.3



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

