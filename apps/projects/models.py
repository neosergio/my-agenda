from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from apps.companies.models import Company


@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=200)
    client = models.ForeignKey(Company, related_name='companies', related_query_name='company')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)
        app_label = 'projects'
        db_table = 'app_projects'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
