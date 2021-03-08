from flask import Flask
from server import app,db

if __name__ == "__main__":

    app.run(host='127.0.0.1', debug=True)



'''
References:
    https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/    flash and html
    https://docs.sqlalchemy.org/en/14/orm/query.html   filter
    https://flask-login.readthedocs.io/en/latest/  loginManager  
    https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/    Error handling
    https://www.w3schools.com/tags/tag_select.asp  Dropdown list
    https://www.w3school.com.cn/html/html_entities.asp 大于号

'''