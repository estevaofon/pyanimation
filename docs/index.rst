Quick Guide
===========
Introduction to the basics

.. image:: /examples/images/spritesheet.png

Create the animation object
-----
Create the animation objecting passing the path to the sprite

.. code-block:: python

    girl = Animation("images/spritesheet.png")

Create the animation
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

the origin of the image is (0,0). The heigh and widht are 125. And we choose to call the animation "run".
.. code-block:: python
    girl.create_animation(0, 0, 125, 125, "run")

Update the Animation
-----
Using it's coordinates
.. code-block:: python
    screen.blit(girl.update_surface(), (girl.x, girl.y))

And it's ready!
.. image:: /examples/images/showcase.gif
