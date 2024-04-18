from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
  
 
  
  email = models.EmailField(max_length=30,unique=True,blank=False,null=False)
  last_name = models.CharField(max_length=20,blank=True,null=True)
  first_name = models.CharField(max_length=20,blank=True,null=True)
  username = models.CharField(max_length=20,blank=False,null=False,unique= True)
  

  
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["username"]

  def __str__(self):
     return f"{self.username}\n{self.email}"

  
  


class Post(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   text = models.TextField(blank=True,null=True)



   
      
   

   
   
    


