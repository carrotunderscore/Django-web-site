from django import forms


class CatForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)  # Field for name with max length of 100 characters
    email = forms.EmailField(label="Email")  # Field for email with email validation


