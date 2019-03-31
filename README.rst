==========
EdmontonPy
==========

A website devoted to promoting Python in Edmonton.

Getting Started
===============

EdmontonPy is a standard Django website. Deployment is done using
EdmontonPy-Ops. To install use pipenv.

.. code-block:: text

    pipenv sync

Get started using EdmontonPy with the ``manage.py`` command.

**Getting a local database configured**
    1. Create your local database
       ``manage.py migrate``
    2. Load data into your database
       ``manage.py loaddata initial_data``

Contributing
============

For guidance on setting up a development environment and how to make a
contribution to EdmontonPy, see the `contributing guidelines`_.

.. _contributing guidelines: https://github.com/EdmontonPy/edmontonpy/blob/master/CONTRIBUTING.rst