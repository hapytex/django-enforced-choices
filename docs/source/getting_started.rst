===============
Getting started
===============

Once the package is installed, you can use the `FullChoicesConstraintModelMixin` mixin in the models, for example:

  .. code-block:: python3

   from django.core.validators import MinValueValidator
   from django.db import models
   from django_enforced_choices import FullChoicesConstraintModelMixin

   
   class Movie(FullChoicesConstraintModelMixin, models.Model):
       genre = models.CharField(max_length=1, choices=[('d', 'drama'), ('h', 'horror')])
       year = models.IntegerField(validators=[MinValueValidator(1888)])

When we then run `makemigrations` it will create a model with the `genre` field, and include a `CheckConstraint` to restrict the values to `'d'` and `'h'`; and the `year` field with a `CheckConstraint` that ensures the value is greater than or equal to 1888.
