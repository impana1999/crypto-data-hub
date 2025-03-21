from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Organization, CryptoPrice
import uuid

class OrganizationAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)

        self.organization = Organization.objects.create(
            id=uuid.uuid4(),
            name="Test Organization",
            created_by=self.user
        )

    def test_create_organization(self):
        data = {"name": "New Org"}
        response = self.client.post("/api/organizations/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_organizations(self):
        response = self.client.get("/api/organizations/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_search_organizations(self):
        response = self.client.get("/api/organizations/?search=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)


    def test_update_organization(self):
        data = {"name": "Updated Org Name"}
        response = self.client.put(f"/api/organizations/{self.organization.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Org Name")

    def test_delete_organization(self):
        response = self.client.delete(f"/api/organizations/{self.organization.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CryptoPriceAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)

        self.organization = Organization.objects.create(
            id=uuid.uuid4(),
            name="Crypto Org",
            created_by=self.user
        )

        self.crypto_price = CryptoPrice.objects.create(
            org=self.organization,
            symbol="BTC",
            price=63000.50
        )

    def test_create_crypto_price(self):
        data = {
            "org": self.organization.id,
            "symbol": "ETH",
            "price": 3500.75
        }
        response = self.client.post("/api/crypto-prices/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_crypto_prices(self):
        response = self.client.get("/api/crypto-prices/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_filter_crypto_prices_by_org(self):
        response = self.client.get(f"/api/crypto-prices/?org_id={self.organization.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_update_crypto_price(self):
        data = {
            "org": self.organization.id,
            "symbol": "BTC",
            "price": 64000.99
        }
        response = self.client.put(f"/api/crypto-prices/{self.crypto_price.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(float(response.data["price"]), 64000.99)

    def test_delete_crypto_price(self):
        response = self.client.delete(f"/api/crypto-prices/{self.crypto_price.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
