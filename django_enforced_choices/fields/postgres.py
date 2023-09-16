from django.contrib.postgres.fields import (
    ArrayField,
    BigIntegerRangeField,
    CICharField,
    CIEmailField,
    CITextField,
    DateRangeField,
    DateTimeRangeField,
    DecimalRangeField,
    HStoreField,
    IntegerRangeField,
    RangeField,
)
from django_enforce_choices.fields import ChoicesConstraintMixin


class ChoiceArrayField(ChoicesConstraintMixin, ArrayField):
    pass


class ChoiceBigIntegerRangeField(ChoicesConstraintMixin, BigIntegerRangeField):
    pass


class ChoiceCICharField(ChoicesConstraintMixin, CICharField):
    pass


class ChoiceCIEmailField(ChoicesConstraintMixin, CIEmailField):
    pass


class ChoiceCITextField(ChoicesConstraintMixin, CITextField):
    pass


class ChoiceDateRangeField(ChoicesConstraintMixin, DateRangeField):
    pass


class ChoiceDateTimeRangeField(ChoicesConstraintMixin, DateTimeRangeField):
    pass


class ChoiceDecimalRangeField(ChoicesConstraintMixin, DecimalRangeField):
    pass


class ChoiceHStoreField(ChoicesConstraintMixin, HStoreField):
    pass


class ChoiceIntegerRangeField(ChoicesConstraintMixin, IntegerRangeField):
    pass


class ChoiceRangeField(ChoicesConstraintMixin, RangeField):
    pass
