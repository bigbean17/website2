from server import db
from models import User, Post

user = User(username="Admin",password="$%j7$#D#$g54y4#$gij$#_98@#", is_admin=True)
db.session.add(user)
db.session.commit()
post = Post(content="Welcome!", uname="Admin")
db.session.add(post)
db.session.commit()