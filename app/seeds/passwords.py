from app.models import db, Password
import datetime


# Adds a demo user, you can add other users here if you want
def seed_passwords():
    yelp = Password(
        website="www.yelp.com",
        emailUser="demo@aa.io",
        password="password",
        name="Yelp",
        user_id=1,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )
    facebook = Password(
        website="www.facebook.com",
        emailUser="demo@aa.io",
        password="password",
        user_id=1,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )
    checking = Password(
        website="www.checking.com",
        emailUser="checking",
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
    db.session.execute("TRUNCATE users RESTART IDENTITY CASCADE;")
    db.session.commit()
