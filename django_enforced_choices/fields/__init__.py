from django.db.models import CheckConstraint, Q
from django.db.models import (
    BigIntegerField,
    BinaryField,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    DecimalField,
    DurationField,
    EmailField,
    FileField,
    FilePathField,
    FloatField,
    GenericIPAddressField,
    ImageField,
    IntegerField,
    JSONField,
    ManyToManyField,
    OneToOneField,
    PositiveBigIntegerField,
    PositiveIntegerField,
    PositiveSmallIntegerField,
    SlugField,
    SmallIntegerField,
    TextField,
    TimeField,
    URLField,
    UUIDField,
)
from django.core.validators import MaxValueValidator, MinValueValidator

CHOICE_CHECK_SUFFIX = "96e824e9"


def add_constraint(model, constraint):
    model._meta.constraints.append(constraint)
    if "constraints" not in model._meta.original_attrs:
        # triggers the migration handler
        model._meta.original_attrs["constraints"] = model._meta.constraints


def add_null(field, constraint, name):
    if constraint is not None and field.null:
        return constraint | Q((f"{name}__isnull", True))
    return constraint


def add_choice_constraint(field, model, name):
    """
    Add a CheckConstraints to the model for which we have a field, which should have choices
    with the given field name. If the field has no .choices, it will not add a constraint.
    If the field is NULLable, it will include this in the check.
    """
    if field.choices is not None:
        constraint_name = f"{field.column}_valid_choices_{CHOICE_CHECK_SUFFIX}"
        if not any(con.name == constraint_name for con in model._meta.constraints):
            # only if the constraint has not been added *yet*
            check = add_null(
                field, Q((f"{name}__in", [k for k, v in field.flatchoices])), name
            )
            add_constraint(model, CheckConstraint(name=constraint_name, check=check))


def get_range_validator(validators, _type):
    # for None
    for validator in validators or ():
        if isinstance(validator, _type):
            limit_value = validator.limit_value
            if callable(limit_value):
                yield limit_value()
            else:
                yield limit_value


def add_range_constraint(field, model, name):
    min_values = list(get_range_validator(field.validators, MinValueValidator))
    if min_values:
        _min = max(min_values)
    else:
        _min = None
    max_values = list(get_range_validator(field.validators, MaxValueValidator))
    if max_values:
        _max = min(max_values)
    else:
        _max = None
    if _min is not None and _max is not None:
        check = Q((f"{name}__range", (_min, _max)))
    elif _min is not None:
        check = Q((f"{name}__gte", _min))
    elif _max is not None:
        check = Q((f"{name}__lte", _max))
    else:
        check = None
    if check is not None:
        check = add_null(field, check, name)
        constraint_name = f"{field.column}_valid_range_{CHOICE_CHECK_SUFFIX}"
        add_constraint(model, CheckConstraint(name=constraint_name, check=check))


class ChoicesConstraintMixin:
    """
    A mixin that can be added to an (arbitrary) model field that will then add a CheckConstraint
    if that field has .choices. It will also, by default, check that choices have been given.
    This check can be disabled by passing check_choices=False. We can omit enforcing choices
    by passing ensure_choices=False.
    """

    def __init__(self, *args, check_choices=True, ensure_choices=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.ensure_choices = ensure_choices
        if check_choices and self.choices is None:
            raise ValueError(f"You need to pass choices for the {type(self)} field")

    def contribute_to_class(self, cls, name, *args, **kwargs):
        super().contribute_to_class(cls, name, *args, **kwargs)
        if self.ensure_choices:
            add_choice_constraint(self, cls, name)


class RangeConstraintMixin:
    """
    A mixin that can be added to an (arbitrary) model field that will then add a CheckConstraint
    if that field has min values or max values (these can have been passed as min_value and max_value,
    but also through MinValueValidator and MaxValueValidator items in the validators parameter).
    """

    def __init__(self, *args, ensure_range=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.ensure_range = ensure_range

    def contribute_to_class(self, cls, name, *args, **kwargs):
        super().contribute_to_class(cls, name, *args, **kwargs)
        if self.ensure_range:
            add_range_constraint(self, cls, name)


class ChoiceBigIntegerField(ChoicesConstraintMixin, BigIntegerField):
    pass


class ChoiceBinaryField(ChoicesConstraintMixin, BinaryField):
    pass


class ChoiceBooleanField(ChoicesConstraintMixin, BooleanField):
    pass


class ChoiceCharField(ChoicesConstraintMixin, CharField):
    pass


class ChoiceDateField(ChoicesConstraintMixin, DateField):
    pass


class ChoiceDateTimeField(ChoicesConstraintMixin, DateTimeField):
    pass


class ChoiceDecimalField(ChoicesConstraintMixin, DecimalField):
    pass


class ChoiceDurationField(ChoicesConstraintMixin, DurationField):
    pass


class ChoiceEmailField(ChoicesConstraintMixin, EmailField):
    pass


class ChoiceFileField(ChoicesConstraintMixin, FileField):
    pass


class ChoiceFilePathField(ChoicesConstraintMixin, FilePathField):
    pass


class ChoiceFloatField(ChoicesConstraintMixin, FloatField):
    pass


class ChoiceGenericIPAddressField(ChoicesConstraintMixin, GenericIPAddressField):
    pass


class ChoiceImageField(ChoicesConstraintMixin, ImageField):
    pass


class ChoiceIntegerField(ChoicesConstraintMixin, IntegerField):
    pass


class ChoiceJSONField(ChoicesConstraintMixin, JSONField):
    pass


class ChoiceManyToManyField(ChoicesConstraintMixin, ManyToManyField):
    pass


class ChoiceOneToOneField(ChoicesConstraintMixin, OneToOneField):
    pass


class ChoicePositiveBigIntegerField(ChoicesConstraintMixin, PositiveBigIntegerField):
    pass


class ChoicePositiveIntegerField(ChoicesConstraintMixin, PositiveIntegerField):
    pass


class ChoicePositiveSmallIntegerField(
    ChoicesConstraintMixin, PositiveSmallIntegerField
):
    pass


class ChoiceSlugField(ChoicesConstraintMixin, SlugField):
    pass


class ChoiceSmallIntegerField(ChoicesConstraintMixin, SmallIntegerField):
    pass


class ChoiceTextField(ChoicesConstraintMixin, TextField):
    pass


class ChoiceTimeField(ChoicesConstraintMixin, TimeField):
    pass


class ChoiceURLField(ChoicesConstraintMixin, URLField):
    pass


class ChoiceUUIDField(ChoicesConstraintMixin, UUIDField):
    pass


class RangeBigIntegerField(RangeConstraintMixin, BigIntegerField):
    pass


class RangeBinaryField(RangeConstraintMixin, BinaryField):
    pass


class RangeBooleanField(RangeConstraintMixin, BooleanField):
    pass


class RangeCharField(RangeConstraintMixin, CharField):
    pass


class RangeDateField(RangeConstraintMixin, DateField):
    pass


class RangeDateTimeField(RangeConstraintMixin, DateTimeField):
    pass


class RangeDecimalField(RangeConstraintMixin, DecimalField):
    pass


class RangeDurationField(RangeConstraintMixin, DurationField):
    pass


class RangeEmailField(RangeConstraintMixin, EmailField):
    pass


class RangeFileField(RangeConstraintMixin, FileField):
    pass


class RangeFilePathField(RangeConstraintMixin, FilePathField):
    pass


class RangeFloatField(RangeConstraintMixin, FloatField):
    pass


class RangeGenericIPAddressField(RangeConstraintMixin, GenericIPAddressField):
    pass


class RangeImageField(RangeConstraintMixin, ImageField):
    pass


class RangeIntegerField(RangeConstraintMixin, IntegerField):
    pass


class RangeJSONField(RangeConstraintMixin, JSONField):
    pass


class RangeManyToManyField(RangeConstraintMixin, ManyToManyField):
    pass


class RangeOneToOneField(RangeConstraintMixin, OneToOneField):
    pass


class RangePositiveBigIntegerField(RangeConstraintMixin, PositiveBigIntegerField):
    pass


class RangePositiveIntegerField(RangeConstraintMixin, PositiveIntegerField):
    pass


class RangePositiveSmallIntegerField(RangeConstraintMixin, PositiveSmallIntegerField):
    pass


class RangeSlugField(RangeConstraintMixin, SlugField):
    pass


class RangeSmallIntegerField(RangeConstraintMixin, SmallIntegerField):
    pass


class RangeTextField(RangeConstraintMixin, TextField):
    pass


class RangeTimeField(RangeConstraintMixin, TimeField):
    pass


class RangeURLField(RangeConstraintMixin, URLField):
    pass


class RangeUUIDField(RangeConstraintMixin, UUIDField):
    pass
