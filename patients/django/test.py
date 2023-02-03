from django.test import Client, TestCase
from .models import Patient
from .transfer import transfer_data
class TransferTestCase(TestCase):
    def setUp(self):
        Patient.objects.create(
            name='John Doe',
            age=30,
            address='123 Main St',
            medical_history='No known conditions',
        )

    def test_transfer(self):
        patient = Patient.objects.get(name='John Doe')
        transfer_data(patient)
        self.assertEqual(Patient.objects.count(), 1)

    def test_views(self):
        client = Client()
        response = client.get('/transfer/')
        self.assertEqual(response.status_code, 302)
        response = client.get('/transfer/confirm/')
        self.assertContains(response, 'Aditya')