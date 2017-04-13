from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from catalog.models import User, Category, Product
from database import Base

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Clear all the tables
session.query(Product).delete()
session.query(User).delete()
session.query(Category).delete()

# Define the categories
seed_categories = [
    Category(name="Atari"),
    Category(name="Super Nintendo"),
    Category(name="Mega Drive"),
    Category(name="Nintendo 64"),
    Category(name="Sega Saturn"),
    Category(name="Dreamcast"),
    Category(name="Playstation"),
    Category(name="GameBoy"),
    Category(name="Playstation 2"),
    Category(name="Xbox 360")
]

# Define some dummy users
seed_users = [
    User(
        username="dummyuser",
        password='h1u2h3981hd89y129h',
        email="dummyuser@test.com",
        name="Dummy",
        avatar="https://pbs.twimg.com/profile_images/2671170543/18debd694829e"
               "d78203a5a36dd364160_400x400.png",
        telephone="+1-202-555-0100"
    ),
    User(
        username="johndoe",
        password='h1u2h3981hd89y129h',
        email="johndoe@test.com",
        name="John Doe",
        avatar="https://pbs.twimg.com/profile_images/2671170543/18debd69"
               "4829ed78203a5a36dd364160_400x400.png",
        telephone="+1-333-222-1111"
    )
]

# Define some dummy products
seed_products = [
    Product(
        title="Nintendo 64 with games",
        description="Selling my Nintendo 64 with 4 games, the video game is"
                    " incredibly well polished and well cared",
        category=seed_categories[3],
        user=seed_users[0],
        picture="products/dummy_product_1.jpg"
    ),
    Product(
        title="Playstation One - Old school :D",
        description="PsOne very well cared"
                    " nice to play some old school games",
        category=seed_categories[6],
        user=seed_users[0],
        picture="products/dummy_product_2.jpg"
    ),
    Product(
        title="Xbox 360 with Kinect",
        description="Selling my baby"
                    " the day has come :(",
        category=seed_categories[9],
        user=seed_users[1],
        picture="products/dummy_product_3.jpg"
    ),
    Product(
        title="Nintendo GameBoy",
        description="GameBoy with Tetris cartdrige",
        category=seed_categories[7],
        user=seed_users[1],
        picture="products/dummy_product_4.jpg"
    )
]


# Seeds the category table
for category in seed_categories:
    session.add(category)
session.commit()

# Seeds the users table
for user in seed_users:
    session.add(user)
session.commit()

# Seeds the products table
for product in seed_products:
    session.add(product)
session.commit()

print "database seeded with success"

