from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib.auth import authenticate
from users.models import Account


class AccountTest(TestCase):
    def test_authenticate_user(self):
        User.objects.create_user(
            username="test1",
            password="secret",
        )
        user = authenticate(username="test1", password="secret")
        self.assertTrue((user is not None) and user.is_authenticated)

    def create_account_test(self):
        user1 = User.objects.create(username="test_user1")
        # user2 = User.objects.create(username="test_user2")
        account1 = Account.objects.create(user=user1)

        self.assertTrue(account1 is not None)
        self.assertEqual(Account.objects.count(), 1)

        user_data = {"username": "created_test_user1", "email": "test@mail.com"}

        account2 = Account.objects.create_account(user_data=user_data)
        self.assertTrue(account2 is not None)
        self.assertEqual(Account.objects.count(), 2)
