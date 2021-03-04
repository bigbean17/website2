from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "HA^=BeQ]Sy1--F^%vBgg@g*Q1s*1`g6<'?r""!N<KyuC~IrGFR0tF$VlKZC,_$m"
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///website2Databse.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import routes