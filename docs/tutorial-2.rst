Guia Rápido
===========
Introdução ao básico

.. image:: /examples/images/link.png

Crie o objeto de animação
-----
Inicialmente precisamos criar o objeto passando o caminho até o arquivo de sprite

.. code-block:: python

    link = Animation("images/link.png")

Configurando a animação
-----
Configure a animação com o método create_animation

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

Vamos construir duas animações dessa sprite.

.. code-block:: python

    link.create_animation(0, 525, 121, 132, "front", duration=90, rows=1)
    link.create_animation(0, 782, 121, 132, "back", duration=90, rows=1)

Atualize a animação
---------------
Atualize a animação no loop do pygame.

.. code-block:: python

    screen.blit(link.update_surface(), (link.x, link.y))

E pronto! Rode o exemplo no seu computador para ver as duas animações geradas.

.. image:: /examples/images/link.gif

O exemplo completo se encontra em `examples\example4.py <https://github.com/estevaofon/pyanimation/blob/master/examples/example4.py>`_
