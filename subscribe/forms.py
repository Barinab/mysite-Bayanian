
from django import forms
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _

class SubscribeFrom(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        labels={ 
            'matn':_('متن'),
            'last_name':_('asd')
            
        }
        error_messages={'first_name':{
            'required':_('yes')
            }}

    

