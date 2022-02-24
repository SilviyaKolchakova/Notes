from django import forms

from notes.web.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'image_url')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'image_url': 'Link to Profile Image',
        }


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title','content', 'image_url')
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image_url': 'Link to Image'
        }
