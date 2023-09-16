from django.db.models import CheckConstraint, Q
from django.db.models import BigIntegerField, BinaryField, BooleanField, CharField, DateField, DateTimeField, DecimalField, DurationField, EmailField, FileField, FilePathField, FloatField, GenericIPAddressField, ImageField, IntegerField, JSONField, ManyToManyField, OneToOneField, PositiveBigIntegerField, PositiveIntegerField, PositiveSmallIntegerField, SlugField, SmallIntegerField, TextField, TimeField, URLField, UUIDField

CHOICE_CHECK_SUFFIX = '96e824e9'


def add_choice_constraint(field, model, name):
    if field.choices is not None:
        constraint_name = f'{field.column}_valid_choices_{CHOICE_CHECK_SUFFIX}'
        if not any(con.name == constraint_name for con in model._meta.constraints):
            # only if the constraint has not been added *yet*
            check = Q((f"{name}__in", [k for k, v in field.flatchoices]))
            if field.null:
                check |= Q((name, None))
            constraint = CheckConstraint(
                name=constraint_name,
                check=check
            )
            model._meta.constraints.append(constraint)
            if 'constraints' not in model._meta.original_attrs:
                # triggers the migration handler
                model._meta.original_attrs['constraints'] = model._meta.constraints


class ChoicesConstraintMixin:

    def __init__(self, *args, ensure_choices=True, **kwargs):
        super().__init__(*args, **kwargs)
        if ensure_choices and self.choices is None:
            raise ValueError(f'You need to pass choices for the {type(self)} field')

    def contribute_to_class(self, cls, name, *args, **kwargs):
        super().contribute_to_class(cls, name, *args, **kwargs)
        add_choice_constraint(self, cls, name)


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


class ChoicePositiveSmallIntegerField(ChoicesConstraintMixin, PositiveSmallIntegerField):
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