from django.urls import reverse, resolve
from django.test import SimpleTestCase
from rest_api.views import TodoItemViewSet
from rest_framework.test import APITestCase,APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
class ApiUrlsTests(SimpleTestCase):

    def test_get_todoItem_is_resolved(self):
        url= reverse('todoitem-list')
        print(resolve(url))
        # self.assertEquals(resolve(url).func.view_class,TodoItemViewSet)

class RestAPIViewTest(APITestCase):
    todoItem_url=reverse('todoitem-list')

    def setUp(self):
        self.user=User.objects.create_user(username="admin",password="password")
        self.token=Token. objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)
        
    def tearDown(self):
        pass
    def test_get_todoItems_authenticated(self):
        response=self.client.get(self.todoItem_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_todoItems_un_authenticated(self):
        self.client.force_authenticate(user=None,token=None)
        response=self.client.get(self.todoItem_url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_post_todoItems_authenticated(self):
        data={
            "title":"testPost",
            "is_completed":True
        }
        response=self.client.post(self.todoItem_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"],"testPost")
    def test_post_todoItems_un_authenticated(self):
        data={
            "title":"testPost",
            "is_completed":True
        }
        self.client.force_authenticate(user=None,token=None)
        response=self.client.post(self.todoItem_url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
