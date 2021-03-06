from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Category(models.Model):
    category_name = models.CharField(max_length = 200)
    category_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_on']
        verbose_name_plural = "categories" 	
        
    def __str__(self):
        return self.category_name
        
class Subscribe(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subscriber_id = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = ["category_id", "subscriber_id"]
    def __str__(self):
        return '{} subscribe to {}'.format(self.subscriber_id, self.category_id)

class Tag(models.Model):
    tag = models.CharField(max_length=30)

    def __str__(self):
        return self.tag
        
class Post(models.Model): 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=1)
    tags =  models.ManyToManyField(Tag, related_name='tags')
    # image = models.ImageField(upload_to='img/', null=True)
    image = models.ImageField(upload_to='images/', null=True)
    
    class Meta:
        ordering = ['-created_on']
        
    def get_tags(self):
        return " ".join([t.tag for t in self.tags.all()])

    def __str__(self):
        return self.title
    #AJAX
    # @classmethod
    # def filter_by_top_likes(cls):
    #     return cls.objects.filter(likes__gt=10).order_by('-created_on')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Reply(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Reply {} by {}'.format(self.body, self.name)

class Likes(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_likes')

class Dislikes(models.Model):
    disliker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dislikes')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_dislikes')

#model for forbidden words
class undesiredWord (models.Model):
    word=models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.word)
