from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accept digits"""
        form = self.make_validated_form(cpf='1asv234')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_capitalized(self):
        """
        Name must be capitalized
        FULANDO de tal -> Fulado de Tal
        """
        form = self.make_validated_form(name='MATHEUS de sousa BarRos')

        words = []

        self.assertEqual('Matheus de Sousa Barros', form.cleaned_data['name'])

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def make_validated_form(self, **kwargs):
        valid = dict(
            name='Matheus de Sousa Barros',
            cpf='12345678901',
            email='bmatheus91@gmail.com',
            phone='98-983868543'
        )

        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
