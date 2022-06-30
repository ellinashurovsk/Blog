from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


class PostsAPIList(ListAPIView):
    """
    View to return a list of all existing posts.

    * Requires JWT token authentication.
    * Only authenticated users are able to access this view.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostAPICreate(CreateAPIView):
    """
    View to create a new post.


    * Requires JWT token authentication.
    * Only authenticated users are able to access this view.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Create a new post.

        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)

        return Response(serializer.data, status=201)


class PostAPIReadUpdateDelete(RetrieveUpdateDestroyAPIView):
    """
    GET: Return a post by it's slug.

    PUT: Update a post by it's slug.

    PATCH: Update a post by it's slug.

    DELETE: Delete a post by it's slug.

    * Requires JWT token authentication.
    * GET - method is allowed for authenticated users,
      PUT, PATCH, DELETE  - methods are allowed only for the post's owner

    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
