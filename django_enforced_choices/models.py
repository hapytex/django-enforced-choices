from django.db import models
from django.db.models.base import ModelBase

# Create your models here.

from .fields import add_choice_constraint


class ChoicesConstraintModelMetaMixin(ModelBase):
    """
    A meta-class with the logic in the _prepare method to inspect the fields, and
    add CheckConstraints for the fields that have choices.
    """

    def _prepare(cls, *args, **kwargs):
        """
        Override the _prepare method to also add CheckConstraints for the corresponding
        fields.
        """
        to_exclude = getattr(cls, "exclude_choice_check_fields", ()) or ()
        super()._prepare(*args, **kwargs)
        for field in cls._meta.fields:
            if field.name not in to_exclude:
                add_choice_constraint(field, cls, field.name)


class ChoicesConstraintModelMixin(metaclass=ChoicesConstraintModelMetaMixin):
    """
    A model mixin, essentially what it does is ensuring that the model inherits
    from the ChoicesConstraintsModelMetaMixin, a subclass of ModelBase, which
    has some extra _prepare logic.
    """

    exclude_choice_check_fields = ()
