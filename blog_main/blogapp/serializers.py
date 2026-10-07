from rest_framework import serializers
from . models import Category,Post,Comment



class CatagorySerializer(serializers.ModelSerializer):
    class Meta : 
        model = Category
        fields = ['id' , 'name','slug']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')
    class Meta:
        model = Comment
        fields = ['id','post','author','content','created_at']
        read_only_fields = ['post' , 'author']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')
    category_details = CatagorySerializer(source = 'category' , read_only = True)
    comments = CommentSerializer(many=True,read_only = True)        

    class Meta :
        model = Post
        fields = [
            'id','author','category_details','comments','category','title','content','image','created_at','updated_at'
        ]



        
          