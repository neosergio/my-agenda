from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from apps.skills.models import Skill
from apps.contacts.models import Contact


@python_2_unicode_compatible
class Level(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, default='', blank=True)
    skills = models.ManyToManyField(Skill, through='LevelSkill', related_name='levels')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        app_label = 'levels'
        db_table = 'app_levels'
        verbose_name = 'Level'
        verbose_name_plural = 'Levels'


@python_2_unicode_compatible
class LevelSkill(models.Model):
    level = models.ForeignKey(Level, related_name='_level')
    skill = models.ForeignKey(Skill, related_name='_skill')
    contact = models.ForeignKey(Contact, related_name='_contact')
    from_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "%s has the level %s in skill %s from %s" % (self.contact, self.level, self.skill, self.from_date)
