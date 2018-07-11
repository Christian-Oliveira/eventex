from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(
            name='Matheus de Sousa Barros',
            cpf='02824886340',
            email='bmatheus91@gmail.com',
            phone='98982858442'
        )

        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_send_subscribe_email(self):
        """Before redirect valid POST, send email to subscriber"""
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email_subject(self):
        """Email subject must be Confirmação de Inscrição"""
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        """Email from must be contato@eventex.com.br"""
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        """Email to must be contato@eventex.com.br and subscribers email"""
        expect = ['contato@eventex.com.br', 'bmatheus91@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        """Email body must contain subscribers information"""
        contents = [
            'Matheus de Sousa Barros',
            '02824886340',
            'bmatheus91@gmail.com',
            '98982858442',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
