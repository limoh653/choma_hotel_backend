from app import app
from database import db
from models.user import User
from models.room import Room

with app.app_context():
    db.create_all()  # Ensure tables exist

    # Add default admin user
    admin = User(username="admin", password="admin123", role="admin")
    db.session.add(admin)

    # Add some sample rooms
    rooms = [
        Room(number="101", type="Single", price=100.0, status="available"),
        Room(number="102", type="Double", price=150.0, status="available"),
        Room(number="103", type="Suite", price=250.0, status="available"),
    ]
    db.session.bulk_save_objects(rooms)

    db.session.commit()
    print("Database seeded successfully!")
