from server import app, db
count_user = 0

class User(db.Model):

    id=db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False, unique=True)
    password = db.Column(db.String(50), nullable = False)



class Post(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = True, unique = False)
    uid = db.Column(db.Integer, db.ForeignKey("user.id"),nullable=False)



def register(username, password):

    user = User(username=username,password=password)
    db.session.add(user)
    db.session.commit()


def login(username,password):

    user = db.session.query(User).filter_by(username=username,password=password).all()
    if(user):
        return True
    return False
