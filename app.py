from flask import Flask
from flask_cors import CORS
from config import Config
from database import db, migrate

# Import models so Alembic can detect them
from models.user import User
from models.room import Room
from models.booking import Booking

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Initialize database and migration
db.init_app(app)
migrate.init_app(app, db)

if __name__ == '__main__':
    app.run(debug=True)
