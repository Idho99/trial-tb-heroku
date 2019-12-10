from django import forms
from imgpro_app.models import TBImage

class TBImageForm(forms.ModelForm):
    """Form definition for TBImage."""

    class Meta:
        """Meta definition for TBImageform."""

        model = TBImage
        fields = ('imgDefault',)
        labels = {'imgDefault':''}
