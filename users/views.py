import json
from typing import TypedDict
from rest_framework.views import APIView
from rest_framework.response import Response

User = TypedDict('User', {'id': int, 'name': str, 'age': int})
File = 'users.json'


class FileTools:
    @property
    def users(self) -> list[User]:
        try:
            with open(File) as file:
                return json.load(file)
        except:
            return []

    @staticmethod
    def save(users: list[User]) -> None:
        with open(File, 'w') as file:
            json.dump(users, file)


class UserListCreateView(APIView, FileTools):
    def get(self, *args, **kwargs):
        return Response(self.users)

    def post(self, *args, **kwargs):
        users = self.users
        new_user = self.request.data
        new_user['id'] = users[-1]['id'] + 1 if users else 1
        users.append(new_user)
        try:
            self.save(users)
        except:
            return Response('Error occurred!')
        return Response(new_user)
