Pyanimation
===========
A python module to easily create animations in pygame

.. image:: https://raw.githubusercontent.com/estevaofon/pyanimation/master/examples/images/spritesheet.png

Setup
-----

.. code-block:: bash

    $ pip install pyanimation

Code sample
-----------

.. code-block:: python

    girl = Animation("images/spritesheet.png")
    girl.create_animation(0, 0, 125, 125, "run")
    screen.blit(girl.update_surface(), (girl.x, girl.y))

Look in the example folder for complete examples.

.. image:: https://raw.githubusercontent.com/estevaofon/pyanimation/master/examples/images/showcase.gif

Quick Guide
-----------

`Tutorial - Portuguese <https://github.com/estevaofon/pyanimation/blob/master/docs/pt/index.rst>`_
