from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import db  

# Initialize Flask app
app = Flask(__name__)

# Configure the database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_management.db'  # Replace with your database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Simple route for testing
@app.route('/')
def index():
    return "Database initialized! Ready for CRUD operations."

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)

