from django.db import models
from django.db.models.base import ModelBase

# Create your models here.

from .fields import add_choice_constraint

class ChoicesConstraintModelMetaMixin(ModelBase):
    def _prepare(cls, *args, **kwargs):
        super()._prepare(*args, **kwargs)
        for field in cls._meta.fields:
            add_choice_constraint(field, cls, field.name)

class ChoicesConstraintModelMixin(metaclass=ChoicesConstraintModelMetaMixin):
    pass


class MyCustomModel(ChoicesConstraintModelMixin, models.Model):
    type = models.CharField(choices=[('a', 'active'), ('q', 'passive')], max_length=1)