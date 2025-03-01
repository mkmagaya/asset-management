from django import forms
from .models import Asset

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_tag', 'name', 'description', 'category', 'purchase_date', 'cost', 'location', 'status']
