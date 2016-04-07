from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Skill(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, default='', blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        app_label = 'skills'
        db_table = 'app_skills'
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
