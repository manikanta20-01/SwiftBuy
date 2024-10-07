from locust import HttpUser, task, between
from random import randint

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        response = self.client.post('/store/carts/')
        if response.status_code == 201:  # Cart created successfully
            result = response.json()
            self.cart_id = result['id']
        else:
            print("Failed to create cart:", response.content)
            self.cart_id = None

    @task(2) 
    def view_products(self):
        collection_id = randint(1, 5)  # Adjust to valid collection IDs
        response = self.client.get(
            f'/store/products/?collection_id={collection_id}', 
            name='/store/products'
        )
        if response.status_code != 200:
            print("Error viewing products:", response.content)

    @task(4)
    def view_product(self):
        product_id = randint(1, 100)  # Adjust to valid product IDs
        response = self.client.get(
            f'/store/products/{product_id}',  # Ensure this is the correct endpoint
            name='/store/products/:id'
        )
        if response.status_code != 200:
            print("Error viewing product:", response.content)

    @task(1)
    def add_to_cart(self):
        if hasattr(self, 'cart_id') and self.cart_id is not None:
            product_id = randint(1, 10)  # Adjust to valid product IDs
            response = self.client.post(
                f'/store/carts/{self.cart_id}/items/',
                name='/store/carts/items',
                json={'product_id': product_id, 'quantity': 1}
            )
            if response.status_code != 201:
                print("Error adding to cart:", response.content)
        else:
            print("Cart ID is not set. Cannot add item to cart.")

    @task
    def say_hello(self):
        response = self.client.get('/playground/hello')
        if response.status_code != 200:
            print("Error saying hello:", response.content)
