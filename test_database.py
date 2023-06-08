import unittest
from engine.database import db, User
from engine.db_mod import add_user
from main import app
from werkzeug.security import generate_password_hash

class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_user(self):
        # Create a user object
        user = User(first_name='Kasumba', last_name='Raymond', email='kasumba@yahoo.com',
                    password='123kkwq',phone_number='+256756519001', account_type='Tutor')

        # Send a POST request to the signup route with user data
        response = self.app.post('/signup', data=user.__dict__)

        # Assert that the response redirects to the login route
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login',response.location)

        # Retrieve the user from the database
        with app.app_context():
            saved_user = User.query.filter_by(email=user.email).first()

        # Assert that the user is saved in the database
        self.assertIsNotNone(saved_user)
        self.assertEqual(saved_user.first_name, user.first_name)
        self.assertEqual(saved_user.last_name, user.last_name)
        self.assertEqual(saved_user.email, user.email)
        #self.assertEqual(saved_user.password, generate_password_hash(user.password))
        self.assertEqual(saved_user.account_type, user.account_type)


if __name__ == '__main__':
    unittest.main()
