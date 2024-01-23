# Splitwise

# Expense Sharing Application
The Expense Sharing Application is a backend service for managing shared expenses among multiple users. Users can add expenses, split them among different participants, and keep track of balances.

## Features

### User Management:
Create and manage user profiles with details like userId, name, email, and mobile number.

### Expense Management:
Add expenses with details such as payer, participants, amount, and type of split (EQUAL, EXACT, PERCENT).
Validate split details based on the type of expense.
Simplify expenses option for balancing.

### Balances:
Calculate and update balances for each user based on expenses and splits.
Retrieve balances for a specific user or all users with non-zero balances.

### Email Notifications:
Send asynchronous email notifications when a new expense is added.
Schedule a weekly email summary with the total amounts owed.
 

# Technologies Used:
Framework: Flask
Database: SQLAlchemy
Caching: Flask-Caching
Background Tasks: Celery
Email Service: Flask-Mail

# API Endpoints:
## User Management:
POST /users: Create a new user.
PUT /users/atharva: Update user details.
GET /users/123: Retrieve user details.

## Expense Management:
POST /expenses: Add a new expense.
GET /expenses/111: Retrieve details of a specific expense.
GET /users/123/expenses: Retrieve expenses for a specific user.

## Balances:
GET /users/123/balances: Retrieve balances for a specific user.
GET /balances: Retrieve balances for all users with non-zero balances.

