from django.db import models
from accounts.models import UserProfile
from django.core.urlresolvers import reverse

# Create your models here.



class Task(models.Model):
    title = models.CharField(max_length = 255, blank = True, null = True)
    user = models.ForeignKey(UserProfile, blank = True, null = True)
    chain = models.IntegerField(default = 0)
    description = models.TextField()
    tag = models.ManyToManyField('Tag', related_name='tasks', null=True, blank=True)
    okayokay = models.TextField(default = 'okayokay')
    
    def __unicode__(self):
        return self.title
  
    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk":self.pk})
    
    def add_chain(self):
        self.chain = self.chain + 1
        self.save()
        # self.chain
    """   
    def chains(self):
        self.chain = self.add_chain()
    """
    '''   
    def chain_true(self):
        self.booleanchain = False
        return self.booleanchain
    '''
#areyouthere should be infinite now ah ok ill try and work around this
    def tfios(self):
        self.okayokay = "okay"
        
    def falsesave(self):
#        if self.okayokay=="okay":
        self.chain = self.chain + 1
        self.okayokay = "okayokay"
        self.save()
        return
        #else:#ok nvm
         #  return
       
        
class Tag(models.Model):
    name = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.name