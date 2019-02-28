from django.forms import ModelForm
from stars.models import Type

# Create the form class.
class MakeForm(ModelForm):
    class Meta:
        model = Type
        fields = '__all__'
