from operator import truediv
from urllib import request
from django.shortcuts import render
import json

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from django.contrib.auth.models import User
from .serializers import PostSerializer, UserSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny


class AllUsers(APIView):
    """
    View to return all existing users.

    * Requires token authentication.
    * Only admin user is able to access this view.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = UserSerializer

    def get(self, request):
        # Return all existing users.

        users = User.objects.all().order_by('id')

        serialized_users = UserSerializer(users, many=True)

        out_data = {
            'success': True,
            'payload': []

        }

        for i in range(len(serialized_users.data)):
            dct = {}
            dct['id'] = serialized_users.data[i]['id']
            dct['username'] = serialized_users.data[i]['username']
            dct['date_joined'] = serialized_users.data[i]['date_joined']
            out_data['payload'].append(dct)

        return Response(out_data)


class CreateUser(APIView):
    """
    View to create a new user.

    * Doesn't require token authentication.
    * Everyone is able to access this view.
    """

    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        # Create a new user.

        in_data = json.loads(request.body)

        username = in_data.get('username')
        password = in_data.get('password')

        # User can provide additional information.
        info = {}
        if 'first_name' in in_data:
            first_name = in_data.get('first_name')
            info['first_name'] = first_name

        if 'last_name' in in_data:
            last_name = in_data.get('last_name')
            info['last_name'] = last_name

        if 'email' in in_data:
            email = in_data.get('email')
            info['email'] = email

        try:
            user = User.objects.get(username=username)

            out_data = {
                'success': False,
                'details': 'Username already exists.'
            }

            return Response(out_data)

        except User.DoesNotExist:

            user = User.objects.create_user(
                username=username, password=password, **info)

            out_data = {
                'success': True,
                'payload': {
                    'id': user.id,
                    'username': user.username
                }
            }

            return Response(out_data, status=201)


class SingleUser(APIView):
    """
    GET: Return a user by it's id.

    PUT: Update a user by it's id.

    PATCH: Update a user by it's id.

    DELETE: Delete a user by it's id.

    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = UserSerializer

    def get(self, request, **kwargs):
        # Return a user by it's id

        current_user = request.user

        try:
            if kwargs['id'] == current_user.id:

                user = User.objects.get(id=kwargs['id'])

                serialized_user = UserSerializer(user, many=False)

                out_data = {
                    'success': True,
                    'payload': {
                        'id': serialized_user.data['id'],
                        'last_login': serialized_user.data['last_login'],
                        'username': serialized_user.data['username'],
                        'first_name': serialized_user.data['first_name'],
                        'last_name': serialized_user.data['last_name'],
                        'email': serialized_user.data['email'],
                        'date_joined': serialized_user.data['date_joined'],
                    }

                }

                return Response(out_data)
            else:
                out_data = {
                    'success': False,
                }
            return Response(out_data)

        except User.DoesNotExist:
            out_data = {
                'success': False,
                'details': "User doesn't exist"
            }
            return Response(out_data)

    def put(self, request, **kwargs):
        # Update a user by it's id.

        current_user = request.user
        in_data = request.data

        user = User.objects.get(id=current_user.id)

        user.username = in_data['username']
        user.password = in_data['password']
        user.first_name = in_data['first_name']
        user.last_name = in_data['last_name']
        user.email = in_data['email']

        user.save()

        serialized_user = UserSerializer(user, many=False)

        out_data = {
            'success': True,
            'payload': {
                'id': serialized_user.data['id'],
                'last_login': serialized_user.data['last_login'],
                'username': serialized_user.data['username'],
                'first_name': serialized_user.data['first_name'],
                'last_name': serialized_user.data['last_name'],
                'email': serialized_user.data['email'],
                'date_joined': serialized_user.data['date_joined'],
            }

        }

        return Response(out_data)

    def patch(self, request, **kwargs):
        # Update a user by it's id.

        current_user = request.user
        in_data = request.data

        user = User.objects.get(id=current_user.id)

        user.username = in_data.get('username', user.username)
        user.password = in_data.get('password', user.password)
        user.first_name = in_data.get('first_name', user.first_name)
        user.last_name = in_data.get('last_name', user.last_name)
        user.email = in_data.get('email', user.email)

        user.save()

        serialized_user = UserSerializer(user, many=False)

        out_data = {
            'success': True,
            'payload': {
                'id': serialized_user.data['id'],
                'last_login': serialized_user.data['last_login'],
                'username': serialized_user.data['username'],
                'first_name': serialized_user.data['first_name'],
                'last_name': serialized_user.data['last_name'],
                'email': serialized_user.data['email'],
                'date_joined': serialized_user.data['date_joined'],
            }
        }

        return Response(out_data)

    def delete(self, request, **kwargs):
        # Delete a user by it's id.

        current_user = request.user

        user = User.objects.get(id=current_user.id)

        user.delete()

        out_data = {
            'success': True,
        }
        return Response(out_data)


################################################################################


class AllPosts(APIView):
    """
    View to return all existing posts.

    * Requires token authentication.
    * Only admin user is able to access this view.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = PostSerializer

    def get(self, request):
        # Return all existing posts.

        posts = Post.objects.all().order_by('id')

        serialized_posts = PostSerializer(posts, many=True)

        print(request.GET)

        out_data = {
            'success': True,
            'payload': []
        }

        for i in range(len(serialized_posts.data)):
            dct = {}
            dct['id'] = serialized_posts.data[i]['id']
            dct['title'] = serialized_posts.data[i]['title']
            dct['slug'] = serialized_posts.data[i]['slug']
            dct['body'] = serialized_posts.data[i]['body']
            dct['date_added'] = serialized_posts.data[i]['date_added']
            dct['owner'] = serialized_posts.data[i]['owner']
            out_data['payload'].append(dct)

        return Response(out_data)


class CreatePost(APIView):
    """
    View to create a new post.


    * Requires token authentication.
    * Only authenticated users are able to access this view.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Create a new post.

        in_data = json.loads(request.body)

        current_user = request.user
        title = in_data.get('title')
        body = in_data.get('body')

        post = Post.objects.create(
            title=title, body=body, owner=current_user)

        serialized_post = PostSerializer(post, many=False)

        out_data = {
            'success': True,
            'payload': serialized_post.data

        }
        return Response(out_data, status=201)


class SinglePost(APIView):
    """
    GET: Return a post by it's slug.

    PUT: Update a post by it's slug.

    PATCH: Update a post by it's slug.

    DELETE: Delete a post by it's slug.

    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = PostSerializer

    def get(self, request, **kwargs):
        # Return a post by it's slug.

        current_user = request.user

        try:
            post = Post.objects.get(
                slug=kwargs['slug'], owner=current_user)

            serialized_post = PostSerializer(post, many=False)

            out_data = {
                'success': True,
                'payload': serialized_post.data

            }

            return Response(out_data)

        except Post.DoesNotExist:
            out_data = {
                'success': False,
                'details': "Post doesn't exist"
            }

            return Response(out_data)

    def put(self, request, **kwargs):
        # Update a post by it's slug.

        current_user = request.user
        in_data = request.data

        post = Post.objects.get(slug=kwargs['slug'], owner=current_user)

        post.title = in_data['title']
        post.body = in_data['body']

        post.save()

        serialized_post = PostSerializer(post, many=False)

        out_data = {
            'success': True,
            'payload': serialized_post.data
        }

        return Response(out_data)

    def patch(self, request, **kwargs):
        # Update a post by it's slug.

        current_user = request.user
        in_data = request.data

        post = Post.objects.get(slug=kwargs['slug'], owner=current_user)

        post.title = in_data.get('title', post.title)
        post.body = in_data.get('body', post.body)

        post.save()
        serialized_post = PostSerializer(post, many=False)

        out_data = {
            'success': True,
            'payload': serialized_post.data
        }

        return Response(out_data)

    def delete(self, request, **kwargs):
        # Delete a post by it's slug.

        current_user = request.user

        post = Post.objects.get(slug=kwargs['slug'], owner=current_user)

        post.delete()

        out_data = {
            'success': True
        }

        return Response(out_data)
