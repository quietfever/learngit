#-*- coding: utf-8 -*-
from django.db import models
#Book {ISBN (PK), Title, AuthorID (FK), Publisher, PublishDate, Price}
#– Author {AuthorID (PK), Name, Age, Country}
# Create your models here.
class Author(models.Model):
        AuthorID = models.CharField(max_length=100)
	Name = models.CharField(max_length=100)
	Age = models.CharField(max_length=100)
	Country = models.CharField(max_length=100)
	def __unicode__(self):
		return self.AuthorID

class Book(models.Model):
	Title = models.CharField(max_length=100)
        AuthorID = models.ForeignKey(Author)
	Isbn = models.CharField(max_length=100)
	Price =	models.CharField(max_length=100)
	Publisher = models.CharField(max_length=100)	
	PublishDate = models.DateField(blank=True,null=True)
	def __unicode__(self):
		return self.Isbn


