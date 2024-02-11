from django import forms

from app.models import JobOffer


class OfferForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = [
            "title",
            "company",
            "location",
            "is_remote",
            "salary",
            "description",
            "url",
        ]
        labels = {"is_remote": "Type"}
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title"}
            ),
            "company": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Company"}
            ),
            "location": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Location"}
            ),
            "is_remote": forms.Select(
                attrs={"class": "form-control", "placeholder": "Type"}
            ),
            "salary": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Salary"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Description",
                    "style": "height: 100px",
                }
            ),
            "url": forms.URLInput(
                attrs={"class": "form-control", "placeholder": "Url"}
            ),
        }
