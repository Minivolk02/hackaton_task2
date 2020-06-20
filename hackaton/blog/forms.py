from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django_comments_xtd.forms import XtdCommentForm


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


class CommentFormWithTitle(XtdCommentForm):
    comment = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'style': 'background-color: green;'}))

    def get_comment_create_data(self, **kwargs):
        data = super(CommentFormWithTitle, self).get_comment_create_data()
        data.update({'comment': self.cleaned_data['comment']})
        return data
