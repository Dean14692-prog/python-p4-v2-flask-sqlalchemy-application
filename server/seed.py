from faker import Faker
from random import choice
from app import app
from models import db, Pet

fake = Faker()

species_list = ['Dog', 'Cat', 'Turtle', 'Hamster', 'Chicken']

with app.app_context():
    print("Clearing existing data...")
    Pet.query.delete()

    print("Seeding 10 pets...")
    for _ in range(10):
        pet = Pet(
            name=fake.first_name(),
            species=choice(species_list)
        )
        db.session.add(pet)

    db.session.commit()
    print("Done seeding.")
