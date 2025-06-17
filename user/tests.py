from django.test import TestCase
from rest_framework.test import APITestCase


# Create your tests here.
# Successfully creates a new user with valid registration data


class HabitViewSetTests(APITestCase):
    def test_successful_user_creation_with_valid_data(self):
        from django.test import RequestFactory
        from django.contrib.auth import get_user_model
        from user.views import UserRegistrationView
        from user.serializers import UserRegistrationSerializer
        import json

        User = get_user_model()
        factory = RequestFactory()

        valid_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'phone': '1234567890',
            'birth_date': '1990-01-01',
            'password': 'testpassword123'
        }

        request = factory.post('/register/',
                               data=json.dumps(valid_data),
                               content_type='application/json')

        view = UserRegistrationView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        created_user = User.objects.get(username='testuser')
        self.assertEqual(created_user.email, 'test@example.com')