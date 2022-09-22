from tkinter import image_names
from rest_framework import serializers
from healandhelp import models

class WebsiteSerializer(serializers.ModelSerializer): 
    class Meta:
        model = models.Website
        fields = '__all__'

        