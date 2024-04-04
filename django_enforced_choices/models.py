from django.db import models
from django.db.models.base import ModelBase

# Create your models here.

from .fields import add_choice_constraint, add_range_constraint


class ConstraintMetaMixin:
    def check_fields(cls, exclude_attribute_name, add_check):
        to_exclude = set(getattr(cls, exclude_attribute_name, ()) or ())
        for field in cls._meta.fields:
            if field.name not in to_exclude:
                add_check(field, cls, field.name)


class ChoicesConstraintModelMetaMixin(ConstraintMetaMixin, ModelBase):
    """
    A meta-class with the logic in the _prepare method to inspect the fields, and
    add CheckConstraints for the fields that have choices.
    """

    def _prepare(cls, *args, **kwargs):
        """
        Override the _prepare method to also add CheckConstraints for the corresponding
        fields.
        """
        super()._prepare(*args, **kwargs)
        cls.check_fields("exclude_choice_check_fields", add_choice_constraint)


class RangeConstraintModelMetaMixin(ConstraintMetaMixin, ModelBase):
    """
    A meta-class with the logic in the _prepare method to inspect the fields, and
    add CheckConstraints for the fields that have choices.
    """

    def _prepare(cls, *args, **kwargs):
        """
        Override the _prepare method to also add CheckConstraints for the corresponding
        fields.
        """
        super()._prepare(*args, **kwargs)
        cls.check_fields("exclude_range_check_fields", add_range_constraint)


class FullConstraintModelMetaMixin(
    ChoicesConstraintModelMetaMixin, RangeConstraintModelMetaMixin, ModelBase
):
    pass


class ChoicesConstraintModelMixin(
    models.Model, metaclass=ChoicesConstraintModelMetaMixin
):
    """
    A model mixin, essentially what it does is ensuring that the model inherits
    from the ChoicesConstraintsModelMetaMixin, a subclass of ModelBase, which
    has some extra _prepare logic.
    """

    exclude_choice_check_fields = ()

    class Meta:
        abstract = True


class RangeConstraintModelMixin(
    models.Model, metaclass=ChoicesConstraintModelMetaMixin
):
    """
    A model mixin, essentially what it does is ensuring that the model inherits
    from the ChoicesConstraintsModelMetaMixin, a subclass of ModelBase, which
    has some extra _prepare logic.
    """

    exclude_range_check_fields = ()

    class Meta:
        abstract = True


class FullChoicesConstraintModelMixin(
    ChoicesConstraintModelMixin,
    RangeConstraintModelMixin,
    models.Model,
    metaclass=FullConstraintModelMetaMixin,
):
    class Meta:
        abstract = True
