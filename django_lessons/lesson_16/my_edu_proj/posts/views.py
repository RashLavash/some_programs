from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from .models import Post 
from .serializers import PostSerializer 

class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated,)
    permission_classes = (IsAdminOrReadOnly,)

    
    def get_permissions(self):
        if self.action == 'create':
            return (IsAuthorOrReadOnly(),)
        return super().get_permissions()
