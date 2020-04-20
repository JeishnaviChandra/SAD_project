from flask import Flask, session, request, render_template
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://cdchsaavgrknuu:7082aaaaa0922b2ca9b64dfc4a129cb135af741f14f814b4731f56ae71fe4d71@ec2-52-71-231-180.compute-1.amazonaws.com:5432/dce88icnef3qtr'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

def main() :
    db.create_all()

if __name__ == "__main__" :

    with app.app_context() :
        main()