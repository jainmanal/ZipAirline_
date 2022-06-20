from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class AccountTests(APITestCase):
    def test_Air_Plane_1(self):
        url = reverse('fuel_details')
        data = {
                'plane_id':[1,2,3,4,5,6,7,8,9],
                'passenger_no':[10,12,15,15,50,12,15,15,50]
                }
        response = self.client.post(url, data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Air_Plane_2(self):
        url = reverse('fuel_details')
        data = {
                'plane_id':[1,2],
                'passenger_no':[10,12]
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_Air_Plane_3(self):
        url = reverse('fuel_details')
        data = {
                'plane_id':[1,2,3,4,8,9],
                'passenger_no':[10,12,1,15,15,50]
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Air_Plane_4(self):
        url = reverse('fuel_details')
        data = {
                'plane_id':[1],
                'passenger_no':[10]
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

