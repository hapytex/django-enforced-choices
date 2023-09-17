===============
Getting started
===============

Once the package is installed, you can use the `ChoicesConstraintModelMetaMixin` mixin in the models, for example:

  .. code-block:: python3
   
   from django.db import models
   from django_enforced_choices import ChoicesConstraintModelMetaMixin

   
   class Movie(ChoicesConstraintModelMetaMixin, models.Model):
       genre = models.CharField(max_length=1, choices=[('d', 'drama'), ('h', 'horror')])

When we then run `makemigrations` it will create a model with the `genre` field, and include a `CheckConstraint` to restrict the values to `'d'` and `'h'`.
