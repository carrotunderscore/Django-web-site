from django import forms
from .models import BlogPost, Projects


class NewPostForm(forms.Form):
    title = forms.CharField(max_length=255, label="Blog Post Title")
    content = forms.CharField(widget=forms.Textarea, label="Content")


class EditPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'form-control-title', }),
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'form-control-content', 'rows': 50}),
        }


class EditProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', "image_url", "github_url", 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'form-control-title', }),
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'id': 'form-control-title', }),
            'github_url': forms.TextInput(attrs={'class': 'form-control', 'id': 'form-control-title', }),
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'form-control-content', 'rows': 50}),
        }


