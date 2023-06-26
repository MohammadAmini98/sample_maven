from flask import Flask, jsonify, request, render_template
#from Flask_CORS import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# postgresql://username:password@host:port/database

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://my_user:A*1CFF@db:5432/database" 


db = SQLAlchemy(app)
#sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Base = declarative_base()
# مدل داده‌ها
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __init__(self, name, email):
        self.name = name
        self.email = email
@app.route('/')
def index():
    return render_template('index.html')
# روت ایجاد کاربر جدید
@app.route('/users', methods=['POST'])
def create_user():
    name = request.json['name']
    email = request.json['email']

    new_user = User(name, email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'})
    

# روت دریافت لیست کاربران
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []

    for user in users:
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
        
        user_list.append(user_data),200
        
    return render_template('users.html', data=user_list)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0',debug=True)
