========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        |
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/decorated_options/badge/?style=flat
    :target: https://readthedocs.org/projects/decorated_options
    :alt: Documentation Status

.. |version| image:: https://img.shields.io/pypi/v/decorated_options.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/decorated_options

.. |downloads| image:: https://img.shields.io/pypi/dm/decorated_options.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/decorated_options

.. |wheel| image:: https://img.shields.io/pypi/wheel/decorated_options.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/decorated_options

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/decorated_options.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/decorated_options

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/decorated_options.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/decorated_options


.. end-badges

Function decorator to make argument passing saner.

* Free software: BSD license

Installation
============

::

    pip install decorated_options

Documentation
=============

https://decorated_options.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
