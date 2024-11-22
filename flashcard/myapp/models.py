from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from enum import Enum
from django.db import models

    
class Difficulty(models.TextChoices):
    EASY = "Easy", "Easy"
    MEDIUM = "Medium", "Medium"
    HARD = "Hard", "Hard"



class FlashCardSet(models.Model):
     name = models.CharField(max_length = 255)
     createdAt = models.DateTimeField(auto_now_add=True)
     updatedAt = models.DateTimeField(auto_now=True)
     def __str__(self):
        return f"FlashCardSet: {self.name}"


class FlashCard(models.Model):
    question = models.CharField(max_length=255, default="Default Question")
    answer = models.CharField(max_length=255, default="Default Answer")
    difficulty = models.CharField(
        max_length=10, 
        choices=Difficulty.choices,
        null=True,
        blank=True 
    )
    set = models.ForeignKey(FlashCardSet, on_delete=models.CASCADE) # check this later
    def __str__(self):
        return f"{self.question}"
 



class User(AbstractUser):  
    admin = models.BooleanField(null=True, default=False) 
    def __str__(self):
        return self.username  



# what the heck is this????????????????????????????
class Collection(models.Model):
    comment = models.TextField(blank=True, null=True)
    set = models.ForeignKey(FlashCardSet, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Collection by {self.author} on {self.set}"



class Comment(models.Model):
    comment = models.TextField()
    flashcard_set = models.ForeignKey('FlashCardSet', on_delete=models.CASCADE)
    author = models.ForeignKey('User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Comment by {self.author}: {self.comment[:50]}..."