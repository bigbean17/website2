from server import app, db, lm
class User(db.Model):

    id=db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False, unique=True)
    password = db.Column(db.String(50), nullable = False)
    is_admin = db.Column(db.Boolean, default=True)
    is_muted = db.Column(db.Boolean, default=False)
    is_blocked = db.Column(db.Boolean, default=False)


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    
    def get_id(self):
        return self.id#Note that this must be a unicode - if the ID is natively an int or some other type, you will need to convert it to unicode. -- from flask doc
    


class Post(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = True, unique = False)
    uname = db.Column(db.String(20), nullable = False)




def register(username, password):

    user = User(username=username,password=password, is_admin=False)
    db.session.add(user)
    db.session.commit()


def login(username,password):

    user = db.session.query(User).filter_by(username=username,password=password).first()
    return user

def savePost(content,username):
    post = Post(content=content,uname=username)
    db.session.add(post)
    db.session.commit()


def getPosts():
    return db.session.query(Post).all()

def getUsers():
    return db.session.query(User).all()

def finduser(username):
    user = db.session.query(User).filter_by(username=username).first()
    return user


@lm.user_loader
def load_user(id):
    return db.session.query(User).filter_by(id=id).first()
