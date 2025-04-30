from django.db import models
# Create your models here.
class Skills(models.Model):
    image = models.ImageField(upload_to='images/');
    name = models.CharField(max_length=100);
    created_at = models.DateTimeField(auto_now_add=True);
    updated_at = models.DateTimeField(auto_now=True);
    
    def __str__(self):
        return self.name

class Project(models.Model):
    project_name = models.CharField(max_length=150);
    project_image = models.ImageField(upload_to='project_image/');
    technologies =  models.ManyToManyField(Skills, related_name="skill");
    project_Desc = models.TextField(default='');
    project_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True);
    update_at = models.DateTimeField(auto_now=True);
    
    def __str__(self):
        return self.project_name