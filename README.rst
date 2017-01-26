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

I often have to write a function which runs a simulation/learning task which I
need to run for several different parameters. This initially is manageable, but
then slowly configuration creep starts to happen: I keep adding more and more
parameters to the functions which run the simulations and keep making my old
code more and more fragile.

I wrote ``decorated_options`` to decouple the arguments for different set of experiments.

In brief,  ``decorated_options`` converts this:

::

    def run(max_num_followers, num_segments, is_hawkes):
        # ...
        # ...

    # tmp = run_multiple_followers(max_num_followers=10, num_segments=10, is_hawkes=True)
    # tmp = run_multiple_followers(max_num_followers=100, num_segments=10, is_hawkes=False)
    # tmp = run_multiple_followers(max_num_followers=10, num_segments=50, is_hawkes=True)
    tmp = run_multiple_followers(max_num_followers=1000, num_segments=100, is_hawkes=False)


to:

::

    from decorated_options import Options, optioned

    @optioned('opts')
    def run(max_num_followers, num_segments, is_hawkes):
        # ...
        # ...


    opts = Options(max_num_followers=10, num_segments=10, is_hawkes=True)
    # tmp = run_multiple_followers(opts=opts)
    # tmp = run_multiple_followers(max_num_followers=100, is_hawkes=False, opts=opts)
    # tmp = run_multiple_followers(num_segments=50, is_hawkes=False, opts=opts)
    tmp = run_multiple_followers(max_num_followers=1000, num_segments=100, is_hawkes=False)



* Benefits over ``**kwargs`` in receiving function:

  1. Early reporting of errors at call-time.
  2. No need to unpack the values.
  3. Default values do not have to be hard-coded.
  4. Allows progressive improvement, no need to change old code which uses positional arguments.

* Benefits over ``**dict`` while calling:

  1. Easier updating/overriding of values
  2. Positional arguments also work
  3. Guaranteed immutability (throws Exceptions on attempted violations.)

* Benefits over default values in receiving function:

  1. ``Options`` objects can save defaults for multiple settings.
  2. De-couples default values from the functions themselves.



Installation
============

::

    pip install git+https://github.com/musically-ut/decorated_options.git@master#egg=decorated_options

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
