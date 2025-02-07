from app.models import db, Password, SCHEMA, environment
import datetime
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_passwords():
    yelp = Password(
        website="www.yelp.com",
        email="demo@aa.io",
        username="demo",
        password="password",
        name="Yelp",
        user_id=1,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )
    facebook = Password(
        website="www.facebook.com",
        email="demo@aa.io",
        username="demo",
        password="password",
        user_id=1,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )
    checking = Password(
        website="www.checking.com",
        username="checking",
        password="Password",
        user_id=1,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )

    db.session.add(yelp)
    db.session.add(facebook)
    db.session.add(checking)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_passwords():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.passwords RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute(text("DELETE FROM businesses"))
    db.session.commit()
