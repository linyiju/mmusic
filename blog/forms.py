from django import forms

from blog.models import Comment, Post


class PostForm(forms.ModelForm):
    """
    Manage blog editing
    """

    class Meta:
        model = Post
        fields = ('title', 'content')


class CommentForm(forms.ModelForm):
    """
    Manage comment
    """

    class Meta:
        model = Comment
        fields = ('author', 'text')
