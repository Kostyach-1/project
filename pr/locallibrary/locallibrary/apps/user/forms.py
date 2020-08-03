from django import forms

from user.models import user

class create_user_form(forms.ModelForm):

    class Meta:
        model = user
        fields = ('job_title', 'user_name', 'user_position', 'user_company', 'user_description')