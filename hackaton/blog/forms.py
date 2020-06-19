from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class IdeaAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label="Контент идеи")

    class Meta:
        model = Idea
        fields = "__all__"

class IdeaForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=CKEditorUploadingWidget(), label="Контент идеи")

    class Meta:
        model = Idea
        exclude = ['vote_score', 'num_vote_up', 'num_vote_down']