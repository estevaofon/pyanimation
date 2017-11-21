Quick Guide
===========
Introduction to the basics

.. raw:: html

    <img src="/examples/images/link.png" width="400px">

Create the animation object
-----
Create the animation objecting passing the path to the sprite file

.. code-block:: python

    link = Animation("images/link.png")

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

At this time we will create to animations

.. code-block:: python

    link.create_animation(0, 525, 121, 132, "front", duration=90, rows=1)
    link.create_animation(0, 782, 121, 132, "back", duration=90, rows=1)

Update the Animation
---------------
Update the animation in the pygame loop. Use the x, y coordinates to place the animation where you want. 


.. code-block:: python

    screen.blit(link.update_surface(), (link.x, link.y))

And it's ready!

.. image:: /examples/images/link.gif

This complete example is at `examples\\example4.py <https://github.com/estevaofon/pyanimation/blob/master/examples/example4.py>`_
