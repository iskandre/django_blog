from django.db import models

INFORMATION_TYPE = (
        ('basic','basic'),
        ('clusters','clusters'),
         ('geography','geography'),
          ('analysis','analysis'),
        ('advanced','advanced')
)

class AccountInfo(models.Model):
    name = models.CharField(max_length=200)
    link_to_files = models.CharField(max_length=200)
    link_to_files1 = models.CharField(max_length=200, default='test')
    resDict_path = models.CharField(max_length=200, default = 'test')
    
    def __str__(self):
        return self.name
    
    
class Statistics(models.Model):
#    informationType = models.CharField(max_length=200,choices = INFORMATION_TYPE, default = 'basic')
    test = models.CharField(max_length=200)
#    account = models.CharField(max_length=200)
#    account = models.ManyToManyField(AccountInfo)
    