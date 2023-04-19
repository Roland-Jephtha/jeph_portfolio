from django.db import models

# Create your models here.

class Education(models.Model):
    title = models.CharField(max_length = 255)
    school = models.CharField(max_length = 255)
    date = models.CharField(max_length = 255)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    

class About(models.Model):
    description = models.TextField()
    
    
    def __str__(self):
        return self.description[0:6]
    

class Skill(models.Model):
    detail = models.TextField()
    
    
    def __str__(self):
            return self.detail[0:6]



class Experience(models.Model):
    company = models.CharField(max_length = 255)
    position = models.CharField(max_length = 255) 
    date  = models.CharField(max_length = 255)
    description = models.TextField()
    
    
    def __str__(self):
            return self.position


class Project(models.Model):
    picture = models.FileField(upload_to = 'media')
    link = models.URLField()
    title = models.CharField(max_length = 255, null = True)
    
    
    def __str__(self):
        return self.title
    
    
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    
    
    def __str__(self):
        return self.name
    
    
    
class Resume(models.Model):
    name = models.CharField(max_length = 255)
    file = models.FileField( null = True, upload_to = 'portfolio-files')
    
    
    def __str__(self):
        return self.name + ' Resume'