from django.db import models
from django.db.models.base import ModelBase

# Create your models here.

from .fields import add_choice_constraint


class ChoicesConstraintModelMetaMixin(ModelBase):
    def _prepare(cls, *args, **kwargs):
        to_exclude = getattr(cls, 'exclude_choice_check_fields', ()) or ()
        super()._prepare(*args, **kwargs)
        for field in cls._meta.fields:
            if field.name not in to_exclude:
                add_choice_constraint(field, cls, field.name)


class ChoicesConstraintModelMixin(metaclass=ChoicesConstraintModelMetaMixin):
    exclude_choice_check_fields = ()
