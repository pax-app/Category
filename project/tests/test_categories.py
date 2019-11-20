import json
import unittest
from datetime import datetime
from project.tests.base import BaseTestCase
from project.api.models import GeneralCategory
from project.api.models import ProviderCategory
from database_singleton import Singleton

db = Singleton().database_connection()


class TestCategoryService(BaseTestCase):
    def test_get_all_gen_categories(self):
        with self.client:
            response = self.client.get('/category/general')
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 200)
            self.assertIn('success', data['status'])

            self.assertEqual(1, data['data']['categories'][0]['id'])
            self.assertIn('Assistência Técnica', data['data']['categories'][0]['name'])
            self.assertEqual(2, data['data']['categories'][1]['id'])
            self.assertIn('Reformas', data['data']['categories'][1]['name'])
            self.assertEqual(3, data['data']['categories'][2]['id'])
            self.assertIn('Serviços Domésticos', data['data']['categories'][2]['name'])
            self.assertEqual(4, data['data']['categories'][3]['id'])
            self.assertIn('Design e Tecnologia', data['data']['categories'][3]['name'])
    def test_get_all_provider_categories(self):
        with self.client:
            response = self.client.get('/category/provider')
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 200)
            self.assertIn('success', data['status'])

            self.assertEqual(1, data['data']['categories'][0]['id'])
            self.assertEqual(1, data['data']['categories'][0]['generalId'])
            self.assertIn('Aparelho de Som', data['data']['categories'][0]['name'])

    def test_get_all_provider_categories_per_general(self):
        with self.client:
            response = self.client.get('/category/provider/1')
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 200)
            self.assertIn('success', data['status'])

            self.assertEqual(1, data['data']['categories'][0]['id'])
            self.assertEqual(1, data['data']['categories'][0]['generalId'])
            self.assertIn('Aparelho de Som', data['data']['categories'][0]['name'])

    def test_get_all_provider_categories_per_general_fail(self):
        with self.client:
            response = self.client.get('/category/provider/7')
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 404)
            self.assertIn('failed', data['status'])
            self.assertIn('ID Not Found', data['error'])

if __name__ == '__main__':
    unittest.main()