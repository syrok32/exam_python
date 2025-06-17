from rest_framework.test import APITestCase


class HabitViewSetTests(APITestCase):
    # GET request to list endpoint returns all products with correct serialization
    def test_list_returns_all_products_with_correct_serialization(self):
        from django.test import RequestFactory
        from shop.views import ProductViewSet
        from shop.models import Product

        product1 = Product.objects.create(name="Product 1", price=10.99, quantity=5)
        product2 = Product.objects.create(name="Product 2", price=20.50, quantity=3)


        factory = RequestFactory()
        request = factory.get('/products/')
        viewset = ProductViewSet()
        viewset.request = request


        response = viewset.list(request)


        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], "Product 1")
        self.assertEqual(response.data[0]['price'], "10.99")
        self.assertEqual(response.data[1]['name'], "Product 2")
        self.assertEqual(response.data[1]['price'], "20.50")

    # GET request to non-existent product ID returns 404 error
    def test_retrieve_non_existent_product_returns_404(self):
        from django.test import RequestFactory
        from django.http import Http404
        from shop.views import ProductViewSet

        # Create request and viewset
        factory = RequestFactory()
        request = factory.get('/products/999/')
        viewset = ProductViewSet()
        viewset.request = request

        # Execute retrieve action with non-existent ID
        with self.assertRaises(Http404):
            viewset.retrieve(request, pk=999)