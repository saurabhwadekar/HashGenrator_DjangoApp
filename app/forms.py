from django import forms



class Get_str_form(forms.Form):
    hash_str = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}),max_length=250)

    