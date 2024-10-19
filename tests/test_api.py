import json
import unittest

from api.database import db
from api.config import TestConfig
from api.seeder import RolesAndClaimsSeeder

from app import app


class UserAPITestCase(unittest.TestCase):
    def setUp(self):
        # Configura aplicação para teste
        self.app = app

        self.app.config.from_object(TestConfig)
        self.client = self.app.test_client()

        self.app_context = self.app.app_context()
        self.app_context.push()

        # Cria o banco de dados em memória
        db.create_all()

    def tearDown(self):
        # Limpa o banco de dados
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_users(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_id(self):
        response = self.client.get('/users/1')
        self.assertEqual(response.status_code, 200)

    def test_post_and_delete_user(self):
        # Executa Seeder antes de testar método POST
        seeder = RolesAndClaimsSeeder()
        seeder.run()

        new_user = {
            "username": "Bob The Tester",
            "email": "bobunittest@email.py",
            "role": "User",
        }

        response = self.client.post(
            '/users/', data=json.dumps(new_user), content_type='application/json')

        self.assertIn("cadastrado com sucesso",
                      response.get_data(as_text=True))

        # Tenta deletar o usuario

        response = self.client.delete('/users/1')

        self.assertIn("Usuario removido",
                      response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
