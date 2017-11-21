Criando Animações com sprites desorganizadas
===========
Muitas vezes as sprites não tem um espaçamento constante, o que inviabiliza fazer a sprite da forma mais automática possível.
Com o pyanimation é possível criar animações nessas situações escolhendo frame por frame.

.. raw:: html

    <img src="/examples/images/goku-ss4.png" width="400px">

Crie o objeto de animação
-----
Inicialmente precisamos criar o objeto passando o caminho até o arquivo de sprite

.. code-block:: python

    goku = Animation("images/goku-ss4.png")

Configurando a animação
-----
Dessa vez precisaremos utilizar o método insert_frame

.. code-block:: python

   def insert_frame(self, xo, yo, sprite_width, sprite_height):
        """
        Insert frame by frame manually
        xo,yo: initial points at the top left corner
        sprite_width,sprite_height: length of sprites
        """

Com o método insert_frame selecionaremos frame por frame que utilizaremos, indicando a origem do frame, e a largura e altura
Depois de escolhidos os frames. Utilizares o método build_animation para montar a animação com frames selecionados.

.. code-block:: python
    def build_animation(self, action_name, repeat=True, duration=40):
        """
        Build Animation from the inserted frames
        and sets a name for the animation
        action_name: a name to an animaiton action
        repeat: True to perform a non-stop animation, False to run just once
        duration: duration of the animation in milliseconds
        """

Para fazer o goku carregando a energia, selecionaremos dois frames, e montaremos a animação com o build animation

.. code-block:: python
    goku.insert_frame(115, 1400, 83, 90)
    goku.insert_frame(195, 1400, 83, 90)
    goku.build_animation("load", repeat=False, duration=250)

115, 1400 é a origem da animação, 83, 90, o comprimento e altura. O repeat=False, faz com que animação rode apenas uma vez.

Atualize a animação
---------------
Atualize a animação no loop do pygame.

.. code-block:: python

    screen.blit(link.update_surface(), (link.x, link.y))

E pronto!

.. image:: /examples/images/goku-ss4.gif

O exemplo completo se encontra em `examples\\example3.py <https://github.com/estevaofon/pyanimation/blob/master/examples/example3.py>`_
