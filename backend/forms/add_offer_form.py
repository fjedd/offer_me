from django import forms
from main_app.models import JobOffer 


class AddOfferForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Job title"}), label="Job title")
    company = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Company"}), label="Company")
    location = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Location"}), label="Location")
    is_remote = forms.CharField(required=True, widget=forms.widgets.Input(attrs={"placeholder": "Job is"}), label="Job is")
    salary = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "salary (range)"}), label="salary (range)")
    description = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Description"}), label="Description")
    url = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Link to job"}), label="Link to")
    
    class Meta:
        model = JobOffer
        exclude = ()