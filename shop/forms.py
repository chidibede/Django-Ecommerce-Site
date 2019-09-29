from django import forms


class checkoutForm(forms.Form):
  Full_name = forms.CharField()
  Address = forms.CharField()
  Phone_number = forms.CharField()
  Email = forms.EmailField()
  CHOICES = (
    ('1', '---'),
    ('2', 'Abia'),
    ('3', 'Abuja'),
    ('4', 'Anambara'),
    ('5', 'Enugu'),
    ('6', 'Imo'),
    ('7', 'Lagos'),
    ('8', 'Rivers'),
  )

  State = forms.ChoiceField(widget=forms.Select, choices=CHOICES)


class contactForm(forms.Form):
  Subject = forms.CharField()
  Full_name = forms.CharField()
  Email = forms.EmailField()
  message = forms.CharField(widget=forms.Textarea)

    