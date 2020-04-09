from django import forms

class TicketRequestForm(forms.Form):
    name = forms.CharField();
    email = forms.EmailField(label='E-mail')
    title = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)
    status = forms.ChoiceField(choices=[('open','Open'),('in progress','In progress', 'closed','Closed')])