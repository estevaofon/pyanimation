Quick Guide
===========
Introduction to the basics

.. image:: /examples/images/spritesheet.png

Create the animation object
-----
Create the animation objecting passing the path to the sprite file

.. code-block:: python

    girl = Animation("images/spritesheet.png")

Setting up the animation
-----
Create the animation setting it's paramenters, the create animation has the signature bellow

.. code-block:: python

    def create_animation(self, xo, yo, sprite_width, sprite_height, action_name, repeat=True, duration=40, **kwargs):
            """
            Create an intire animation and sets a label to the animation
            xo,yo: initial points at the top left corner
            sprite_width,sprite_height: length of sprites
            action_name: a name to an animaiton action
            repeat: True to perform a non-stop animation, False to run just once
            duration: duration of the animation in milliseconds

            Optional kwargs
            to use just some slices of a sprite image
            rows: a row is an horizontal sequence of sprites
            cols: the vertical separation of sprites
            """

The origin of the image is xo=0, and y0=0. Each sprite or frame of this image has a widht=125 and a height =125. And we choose to call the animation "run". Which Animation object can have multiple animations actions for example run, punch, kick, etc. You can name it whatever you want.

.. code-block:: python

    girl.create_animation(0, 0, 125, 125, "run")

Update the Animation
---------------
Update the animation in the pygame loop. Use the x, y coordinates to place the animation where you want. 

.. code-block:: python

    screen.blit(girl.update_surface(), (girl.x, girl.y))

And it's ready!

.. image:: /examples/images/showcase.gif

This complete example is at `examples\\example1.py <https://github.com/estevaofon/pyanimation/blob/master/examples/example1.py>`_

`Example 2 - Animation of the Link from Zelda <https://github.com/estevaofon/pyanimation/blob/master/docs/tutorial-2.rst>`_
