from rest_framework import viewsets,permissions,filters
from . models import Category,Post,Comment
from . serializers import CatagorySerializer,PostSerializer,CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from . permissions import IsOwnerOrRreadOnly

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CatagorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrRreadOnly]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['title' , 'content']
    ordering_fields = ['created_at']

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrRreadOnly]
    def get_queryset(self):
        
       post_id = self.request.query_params.get('post_id')

       if post_id:
           return self.queryset.filter(post_id = post_id)
       return self.queryset
    def perform_create(self,serializer):
            serializer.save(author=self.request.user)
            