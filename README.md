# Django-enforced-choices

[![PyPi version](https://badgen.net/pypi/v/django-enforced-choices/)](https://pypi.python.org/pypi/django-enforced-choices/)
[![Documentation Status](https://readthedocs.org/projects/django-enforced-choices/badge/?version=latest)](http://django-enforced-choices.readthedocs.io/?badge=latest)
[![PyPi license](https://badgen.net/pypi/license/django-enforced-choices/)](https://pypi.python.org/pypi/django-enforced-choices/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Django does *not* enforce choices at the model level: yes a `ModelForm` can validate these, but unfortunately people oftend define form fields themselves or even worse don't work with any `Form` or `Serializer` at all. So this means that if we define a model:

```
class Movie(models.Model):
    genre = models.CharField(max_length=1, choices=[('d', 'drama'), ('h', 'horror')])
```

The database will *not* enforce that one can only pick `'d'` or `'h'` as genre. A simple solution might be to encapsulate the item in a separate model, and then the `FOREIGN KEY` constraint will take care of this:

```
class Genre(models.Model):
  id = models.CharField(max_length=1, primary_key=True)
  name = models.CharField(max_length=128)


class Movie(models.Model):
  genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
```

we can then fill the table with a data migration for example. This also makes some sense: a quote I once heared is that there should only be three constants in programming: zero, one and infinity, meaning that typically one should not restrict the number of genres.

But regardless, people often use the former model. This is good if we work with `Form`s, or `Serializer`s, but models don't (eagerly) validate data, and even if they did, the database does not know about the choices, and thus will happily accept `'s'` as value (for example for science fiction).

## What does this package provide?

This package provides a `ChoicesConstraintModelMixin` mixin to mix into models. This will look for the model fields, and if there are choices it will add `CheckConstraint`s for these fields. One can exclude certain fields that have choices by adding the corresponding names in a class attribute named `exclude_choice_check_fields`, which is by default empty.

Another option is to import the correspond field from the `django_enforced_choices.fields` module, or `django_enforced_choices.fields.postgres` for PostgreSQL-specific fields. This will, by default, also check if the fields have choices, but we do *not* recommend to use these, since this means the field has for example as type `ChoiceCharField`, and certain Django functionalities (and packages) sometimes check full type equality to determine a widget, not through an `instanceof`. This thus means that certain functionalities might no longer work as intended.

### Usage

One can import the `ChoicesConstraintModelMixin` and mix it into a model, like:

```
from django_enforced_choices.models import ChoicesConstraintModelMixin

class Movie(ChoicesConstraintModelMixin, models.Model):
    genre = models.CharField(max_length=1, choices=[('d', 'drama'), ('h', 'horror')])
```

this will then add `CheckConstraint`s to the model to enforce that `genre` only can contain `'d'` and `'h'` at the database side.

## How does the package work?

For the fields defined, it will check if the `choices` are defined. If that is the case, it will create a `CheckConstraint` with `fieldname__in` with the keys in the choices. If the field is NULLable, it will also allow `NULL`/`None` to be used.
