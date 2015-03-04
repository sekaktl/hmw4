from tastypie import fields
from tastypie.resources import ModelResource
from blogapp.models import Post
from blogapp.models import Comment


class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'


class CommentResource(ModelResource):
    post = fields.ForeignKey(PostResource, 'post')
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
