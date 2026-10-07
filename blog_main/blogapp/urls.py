from django.urls import path,include
from rest_framework.routers import DefaultRouter 
from . import views

router = DefaultRouter()
router.register(r'category',views.CategoryViewSet , basename = 'category')
router.register(r'post', views.PostViewSet , basename = 'Post')
router.register( r'comments' ,views.CommentViewSet , basename = 'comments' ) 


urlpatterns = [
    path( '' , include(router.urls))
    
]
