from flask import Flask
from server import app,db

if __name__ == "__main__":

    app.run(host='127.0.0.1', debug=True)
