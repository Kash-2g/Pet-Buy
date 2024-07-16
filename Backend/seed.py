from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from app import app, db, User, Buy, Breeds, Activity

# Initialize Faker (optional, for generating fake data)
fake = Faker()

def delete_data():
    """Delete existing data from the database."""
    with app.app_context():
        db.session.query(Buy).delete()
        db.session.query(Breeds).delete()
        db.session.query(User).delete()
        db.session.query(Activity).delete()
        db.session.commit()
        print("Existing data deleted successfully!")

def seed_data():
    """Seed the database with sample data."""
    with app.app_context():
        # Create users
        user1 = User(username='john', password='password', email='john@example.com')
        user2 = User(username='jane', password='password', email='jane@example.com')

        # Add users to the session
        db.session.add_all([user1, user2])
        db.session.commit()

        # Create activities
        activitiesList = [
            "White fur coat",
            "Blue eyes",
            "Curly tail",
            "Floppy ears",
            "Pink nose",
            "Dark brown eyes",
            "Large paws"
        ]

        for activity_name in activitiesList:
            activity = Activity(name=activity_name)
            db.session.add(activity)
        
        db.session.commit()

        # Create Buys
        Buy1 = Buy(name='Bench Press', email='john@example.com', address='123 Main St', contacts='John Doe', user_id=user1.id)
        Buy2 = Buy(name='Yoga Class', email='jane@example.com', address='456 Oak Ave', contacts='Jane Smith',  user_id=user2.id)

        db.session.add_all([Buy1, Buy2])
        db.session.commit()

        # Seed breeds using breedsData
        breedsData = [
            {
                "name": 'German Shepherd',
                "specialty": 'Guard Dog',
                "image": 'https://i.pinimg.com/originals/b2/86/17/b28617b2785c956c01162c35b1c48b4f.jpg',
            },
            {
                "name": 'Beagle',
                "specialty": 'Hunting Dog',
                "image": 'https://i.pinimg.com/originals/b2/c0/7b/b2c07baaf174e477130342ac9f4840df.jpg',
            },
            {
                "name": 'Belgian Malinois',
                "specialty": 'Guard Dog',
                "image": 'https://i.pinimg.com/originals/a3/17/c3/a317c32ac62fd9f1574064a91eaa40dc.jpg',
            },
            {
                "name": 'Rottweiler',
                "specialty": 'Guard Dog',
                "image": 'https://i.pinimg.com/originals/8c/d6/19/8cd6198fa7c83d7347c1978979610960.jpg',
            },
            {
                "name": 'Chihuahua',
                "specialty": 'Companion Dog',
                "image": 'https://i.pinimg.com/originals/4e/4a/9f/4e4a9fcd43bae1114483d01b3ac7acea.jpg',
            },
            {
                "name": 'Doberman Pinscher',
                "specialty": 'Guard Dog',
                "image": 'https://i.pinimg.com/originals/06/2f/dc/062fdcadc88ca9eb958b96697768dc61.jpg',
            },
            {
                "name": 'Boerboel',
                "specialty": 'Working Dog',
                "image": 'https://i.pinimg.com/originals/24/e3/e7/24e3e7a0e475a8e59250d04bf644e2a3.jpg',
            },
            {
                "name": 'Dobermann',
                "specialty": 'Guard Dog',
                "image": 'https://i.pinimg.com/originals/67/e8/b1/67e8b1a74fcab211486d34aabc340dcd.jpg',
            },
        ]

        for data in breedsData:
            breed = Breeds(name=data['name'], speciality=data['specialty'], image=data['image'])
            db.session.add(breed)
        
        db.session.commit()

        print("Seed data has been added successfully!")

if __name__ == '__main__':
    delete_data()  # Delete existing data before seeding (optional)
    seed_data()    # Seed the database with sample data