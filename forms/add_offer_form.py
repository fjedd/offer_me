from __future__ import annotations

from django import forms

from main_app.models import JobOffer


class AddOfferForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = [
            'title',
            'company',
            'location',
            'is_remote',
            'salary',
            'description',
            'url',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'is_remote': forms.Select(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
        }
