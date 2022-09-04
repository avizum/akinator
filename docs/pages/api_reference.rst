.. py:currentmodule:: asyncakinator


API Reference
=============

Akinator
--------
.. autoclass:: Akinator
    :members:

Models
------
.. autoclass:: Answer
    :members:

.. autoclass:: Language
    :members:

.. autoclass:: Theme
    :members:

.. autoclass:: Guess
    :members:
    :exclude-members:

Utils
-----

MISSING
~~~~~~~
.. attribute:: akinator.utils.MISSING

A sentinel value that is used to indicate a missing value with distinction from :class:`None`.


Exceptions
----------

InvalidAnswerError
~~~~~~~~~~~~~~~~~~
.. autoclass:: InvalidAnswerError
    :members:

InvalidLanguageError
~~~~~~~~~~~~~~~~~~~~
.. autoclass:: InvalidLanguageError
    :members:

AkinatorConnectionFailure
~~~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: AkinatorConnectionFailure
    :members:

AkinatorTimeout
~~~~~~~~~~~~~~~
.. autoclass:: AkinatorTimeout
    :members:

AkinatorNoQuestions
~~~~~~~~~~~~~~~~~~~
.. autoclass:: AkinatorNoQuestions
    :members:

AkinatorServerDown
~~~~~~~~~~~~~~~~~~
.. autoclass:: AkinatorServerDown
    :members:

AkinatorTechnicalError
~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: AkinatorTechnicalError
    :members:

CantGoBackAnyFurther
~~~~~~~~~~~~~~~~~~~~
.. autoclass:: CantGoBackAnyFurther
    :members:
