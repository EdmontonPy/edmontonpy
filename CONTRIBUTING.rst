=======================================
Appriciating your valuable contribution
=======================================

Thank you for considering contributing to EdmontonPy. It is people like you
that make this community what it is. Following these guidelines helps to
communicate that you respect the time of the developers managing and developing
this open source project. In return, they should reciprocate that respect in
addressing your issue, assessing changes, and helping you finalize your pull
requests.

EdmontonPy is an open source project, and we love to receive contributions from
our community. There are many ways to contribute, from orginizing issues,
improving the documentation, submitting bug reports, providing feature
requests, writing code or even presenting at the EdmontonPy meetup itself.

Please, don't use the issue tracker for support questions. Check whether the
#meetup channel on edmontonpy.slack.com can help with your issue. If your
problem is related to security please email edmonton.py@gmail.com.

All development is done in compliance with PEP8 and full coverage.

Getting Started
===============

This section will go through the steps on how to get started contributing to
EdmontonPy.

1. Download and install the latest version of git
2. Configure git with your username and email

.. code-block:: text

    git config --global user.name 'your name'
    git config --global user.email 'your email'

3. Make sure you have a GitHub account
4. Fork edmontonpy to your GitHub account by clicking the Fork button
5. Clone your GitHub fork locally

.. code-block:: text

    git clone https://github.com/{username}/edmontonpy
    cd edmontonpy

6. Add the main repository as a remote to update later

.. code-block:: text

    git remote add edmontonpy https://github.com/EdmontonPy/edmontonpy
    git fetch edmontonpy

7. Use pipenv and npm to install the project in development mode

.. code-block:: text

    pipenv sync --dev
    npm install

8. Create a branch to identify the issue you would like to work on

.. code-block:: text

    git branch {issue number}-{issue title}
    git checkout {issue number}-{issue title}

9. Include tests that cover any code changes. Make sure the test fails without
   your patch. Run the tests..

.. code-block:: text

    ./bin/run_tests

10. Using your favorite editor, make your changes, committing as you go
11. Push your commits to GitHub and create a pull request, if your changes
    inculde interface changes; please also submit screenshots of the affected
    pages.

Reporting issues
================

If you find a security vulnerability, do NOT open an issue. Please email
edmonton.py@gmail.com instead. In order to determine whether you are dealing
with a security issue, ask yourself these two questions:

1. Can I access something I shouldn't have access to?
2. Can I disable something for other people?

If the answer to either of those two questions are "yes", then you're probably
dealing with a security issue. Even if you answer "no" to both questions, you
may still be dealing with a security issue, if you're unsure, email us at
edmonton.py@gmail.com.

When filing an issue, make sure to answer these three questions:

1. What did you do?
2. What did you expect to see?
3. What did you see instead?

General questions should go to the #meetup channel on edmontonpy.slack.com.

Suggest a feature or enhancement
================================

If you find yourself wishing for a feature that doesn't exist in EdmontonPy,
you are probably not alone. There are bound to be others out there with similar
needs. Many of the features that EdmontonPy has today have been added because
our users saw the need. Open an issue on our issues list on GitHub which
describes the feature you would like to see, why you need it, and how it should
work.

Compilation
===========

SCSS compilation is done using npm to produce ``style.min.scss``; run
``npm run dist`` after you have installed the npm requirements.

Tests
=====

Tests can be called with ``./bin/run_tests``.
