from flask import Flask

app = Flask(__name__)

from app import routes

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5000)  # Change the port if you're using a different one