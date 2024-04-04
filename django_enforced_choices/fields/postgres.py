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
from django_enforce_choices.fields import ChoicesConstraintMixin, RangeConstraintMixin


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


class RangeArrayField(RangeConstraintMixin, ArrayField):
    pass


class RangeBigIntegerRangeField(RangeConstraintMixin, BigIntegerRangeField):
    pass


class RangeCICharField(RangeConstraintMixin, CICharField):
    pass


class RangeCIEmailField(RangeConstraintMixin, CIEmailField):
    pass


class RangeCITextField(RangeConstraintMixin, CITextField):
    pass


class RangeDateRangeField(RangeConstraintMixin, DateRangeField):
    pass


class RangeDateTimeRangeField(RangeConstraintMixin, DateTimeRangeField):
    pass


class RangeDecimalRangeField(RangeConstraintMixin, DecimalRangeField):
    pass


class RangeHStoreField(RangeConstraintMixin, HStoreField):
    pass


class RangeIntegerRangeField(RangeConstraintMixin, IntegerRangeField):
    pass


class RangeRangeField(RangeConstraintMixin, RangeField):
    pass
