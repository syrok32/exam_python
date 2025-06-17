from rest_framework.test import APITestCase, APIClient
from shop.models import Product

class ProductViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()

    # GET request to list endpoint returns all products with correct serialization
    def test_list_returns_all_products_with_correct_serialization(self):
        product1 = Product.objects.create(name="Product 1", price=10.99, quantity=5)
        product2 = Product.objects.create(name="Product 2", price=20.50, quantity=3)

        response = self.client.get('/products/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], "Product 1")
        self.assertEqual(response.data[0]['price'], "10.99")
        self.assertEqual(response.data[1]['name'], "Product 2")
        self.assertEqual(response.data[1]['price'], "20.50")

    # GET request to non-existent product ID returns 404 error
    def test_retrieve_non_existent_product_returns_404(self):
        response = self.client.get('/products/999/')
        self.assertEqual(response.status_code, 404)