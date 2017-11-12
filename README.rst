Pyanimation
===========
A python module to easily create animations in pygame

.. image:: /examples/images/spritesheet.png


Setup
-----

.. code-block:: bash

    $ pip install pyanimation

Code sample
-----

.. code-block:: python

    girl = Animation("images/spritesheet.png")
    girl.create_animation(0, 0, 125, 125, 4, "run", duration=50, rows=4)
    screen.blit(girl.update_surface(), (girl.x, girl.y))

Look in the example folder for complete examples.

.. image:: /examples/images/showcase.gif
