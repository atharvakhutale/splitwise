from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CACHE_TYPE'] = 'simple'
app.config['MAIL_SERVER'] = 'http://127.0.0.1:8000'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'atharva'
app.config['MAIL_PASSWORD'] = '123atharva'

db = SQLAlchemy(app)
cache = Cache(app)
mail = Mail(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    mobile_number = db.Column(db.String(15), nullable=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10), nullable=False)
    split_details = db.Column(db.String(255), nullable=False)

def send_email(subject, recipients, body):
    with app.app_context():
        msg = Message(subject, recipients=recipients)
        msg.body = body
        mail.send(msg)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.json
    new_expense = Expense(**data)
    db.session.add(new_expense)
    db.session.commit()

    # email notification
    recipients = [user.email for user in User.query.all()]
    subject = f'Expense Notification: New Expense Added'
    body = f'You have been added to a new expense. You owe {data["amount"]} for this expense.'
    send_email.delay(subject, recipients, body)

    return jsonify({'message': 'Expense added successfully'}), 201


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
