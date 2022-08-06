from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from django.test import Client
# Create your tests here.

class TodoTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test_user',  password= 'Qweasdzxc123')
        self.client = Client()
        
        Task.objects.create(user=self.user, title="Some test task1", 
                            description='some long and boring descriprion',
                            complete=False
                            )
        Task.objects.create(user=self.user, title="Some test task2", 
                            description='Even longer description',
                            complete=True
                            )
    
    def test_task_list(self):
        self.client.force_login(self.user)
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
    
    def test_api_get(self):
        self.client.force_login(self.user)
        response = self.client.get('/api/')
        self.assertEqual(response.json()[0]['title'], "Some test task1")

    def test_api_delete(self):
        self.client.force_login(self.user)
        self.client.delete('/api/1/')
        response = self.client.get('/api/')
        self.assertEqual(len(response.json()), 1)

    def test_api_patch(self):
        self.client.force_login(self.user)
        resp_initial = self.client.get('/api/')
        resp_initial_json = resp_initial.json()
        pr = self.client.patch(f'/api/{resp_initial_json[0]["id"]}/', data ={
                                        "complete": True},  content_type='application/json')
        response = self.client.get('/api/')
        self.assertEqual(response.json()[0]['complete'], True)

    def test_api_post(self):
        self.client.force_login(self.user)
        self.client.post('/api/', data ={
                                        "user": self.user.id,
                                        "title":"Some test task3", 
                                        "description":"some long and boring descriprion of task3",
                                        "complete": False},  content_type='application/json')
        response = self.client.get('/api/')
        self.assertEqual(len(response.json()), 3)