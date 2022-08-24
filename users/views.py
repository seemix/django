from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class Test(APIView):
    def get(self, request):
        return Response('GET METHOD')


# Create your views here.
users = [
    {'id': 1, 'name': 'Vasya', 'age': 30},
    {'id': 2, 'name': 'Petya', 'age': 40},
    {'id': 3, 'name': 'Misha', 'age': 20}
]


class UserListCreateView(APIView):
    def get(self, request):
        return Response(users)

    def post(self, *args, **kwargs):
        new_user = self.request.data
        users.append(new_user)
        return Response(self.request.data)


class UserRetrieveUpdateDestroy(APIView):
    def get(self, *args, **kwargs):
        user_id = kwargs.get('id')
        for user in users:
            if user['id'] == user_id:
                return Response(user)
        return Response('Not Found')
