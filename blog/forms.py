from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()

    content = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "rows":"5",
            "placeholder": "Hãy để lại 1 bình luận!"
        })
    ) 

    class Meta:
        model = Comment
        fields = ('content',)