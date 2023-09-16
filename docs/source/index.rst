=======================
Django enforced choices
=======================

django-enforced-choices is a Django library that adds a CheckConstraint for fields
with choices, such that the database guarantees that the choices are valid.

**Features:**

   * a mixin that will check for all fields in the model with choices that the choices are valid.

   * subclasses of all standard model fields with a choice variant to ensure that the choices are valid, this can be used to check a single field.


.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   getting_started

.. toctree::
   :maxdepth: 2
   :caption: API documentation

   api_models
   api_fields
   api_fields_postgres


.. _`tablib`: https://github.com/jazzband/tablib
