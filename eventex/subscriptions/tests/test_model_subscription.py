from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime


class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name='Fulano de Tal',
            cpf='12345678901',
            email='bmatheus91@gmail.com',
            phone='98-983868543'
        )
        self.obj.save()

    def test_create(self):
        """Check if the object was saved"""

        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have a created_at attribute"""
        self.assertIsInstance(self.obj.created_at, datetime)
