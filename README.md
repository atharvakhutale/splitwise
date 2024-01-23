# splitwise

Expense Sharing Application
The Expense Sharing Application is a backend service for managing shared expenses among multiple users. Users can add expenses, split them among different participants, and keep track of balances.

Features
User Management:

Create and manage user profiles with details like userId, name, email, and mobile number.
Expense Management:

Add expenses with details such as payer, participants, amount, and type of split (EQUAL, EXACT, PERCENT).
Validate split details based on the type of expense.
Simplify expenses option for balancing.
Balances:

Calculate and update balances for each user based on expenses and splits.
Retrieve balances for a specific user or all users with non-zero balances.
Email Notifications:

Send asynchronous email notifications when a new expense is added.
Schedule a weekly email summary with total amounts owed.
Technologies Used
Framework: Flask
Database: SQLAlchemy
Caching: Flask-Caching
Background Tasks: Celery
Email Service: Flask-Mail
Getting Started
Installation:

bash
Copy code
pip install -r requirements.txt
Database Setup:

bash
Copy code
flask db init
flask db migrate
flask db upgrade
Configuration:

Update the configuration in config.py with your mail server details.
Run the Application:

bash
Copy code
flask run
Run Celery for Background Tasks:

bash
Copy code
celery -A app.celery worker --loglevel=info
API Endpoints
User Management:

POST /users: Create a new user.
PUT /users/{userId}: Update user details.
GET /users/{userId}: Retrieve user details.
Expense Management:

POST /expenses: Add a new expense.
GET /expenses/{expenseId}: Retrieve details of a specific expense.
GET /users/{userId}/expenses: Retrieve expenses for a specific user.
Balances:

GET /users/{userId}/balances: Retrieve balances for a specific user.
GET /balances: Retrieve balances for all users with non-zero balances.
Contributing
Feel free to contribute to the development of this project. Check the CONTRIBUTING.md file for more information.
