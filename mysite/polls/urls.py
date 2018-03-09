# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 00:38:09 2018

@author: nghia
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]