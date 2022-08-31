from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status

from .models import UserModel
from .serializers import UserSerializer


class UserListCreateView(APIView):
    def get(self, *args, **kwargs):
        qs = UserModel.objects.all()
        # res = [model_to_dict(user) for user in qs]
        serializer = UserSerializer(qs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        # new_user = UserModel(**data)
        # new_user.save()
        serializer = UserSerializer(data=data)
        # if not serializer.is_valid():
        #    return Response(serializer.errors)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')

        # qs = UserModel.objects.filter(pk=pk)
        # exists = qs.exists()
        # if not exists:
        #     return Response('User not found!')
        # user = qs.first()
        user = get_object_or_404(UserModel, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        data = self.request.data
        serializer = UserSerializer(user, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # qs = UserModel.objects.filter(pk=pk)
        # exists = qs.exists()
        # if not exists:
        #     return Response('User not found!')
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        data = self.request.data
        serializer = UserSerializer(user, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        user.delete()
        # qs = UserModel.objects.filter(pk=pk)
        # exists = qs.exists()
        # if not exists:
        #     return Response('User not found!')
        # user = UserModel.objects.get(pk=pk)
        # user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
