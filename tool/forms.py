from django import forms
from tool.models import Statistics
from tool.models import AccountInfo
from material import Layout, Row, Fieldset

# Create your models here.
INFORMATION_TYPE = (
        ('basic','basic'),
        ('clusters','clusters'),
         ('geography','geography'),
          ('analysis','analysis'),
        ('advanced','advanced')
)

class showStatisticsForm(forms.ModelForm):
#    name = forms.charField(max_length=200)
#    accountType = forms.MultipleChoiceField(choices=['text1','text1'], widget=forms.CheckboxSelectMultiple())
#    relationSearch = forms.ModelMultipleChoiceField(
#            widget = forms.CheckboxSelectMultiple,
#            required = True
#            )
    informationType = forms.ChoiceField(choices=INFORMATION_TYPE)
    account = forms.ModelChoiceField(queryset=AccountInfo.objects.all())
    
    class Meta:
        model = Statistics
       
        fields = ['informationType','test','account']
#        widgets = {
##                'relationSearch':forms.CheckboxSelectMultiple(),
#                'account' : forms.ModelChoiceField(queryset=AccountInfo.objects.all())
#                }
           
    layout = Layout(
            Fieldset("Select your account",
                 'informationType','test','account'))
    
#    def save(self, commit=True):
#        # do something with self.cleaned_data['temp_id']
#        return super(Statistics, self).save(commit=commit)