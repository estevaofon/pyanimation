Guia Rápido
===========
Introdução ao básico

.. image:: /examples/images/spritesheet.png

Criação do objeto Animation
-----
Crie o objeto Animation fornecendo o caminho para o arquivo de sprite

.. code-block:: python

    girl = Animation("images/spritesheet.png")

Definindo a Animação
-----
Defina a animação através do método create_animation abaixo

.. code-block:: python

    def create_animation(self, xo, yo, sprite_width, sprite_height, action_name, repeat=True, duration=40, **kwargs):
            """
            xo,yo: Pontos iniciais no canto superior esquerdo
            sprite_width,sprite_height: Largura e altura da sprite
            action_name: Nome da ação
            repeat: Verdadeiro para repetir sem parar, Falso para rodar apenas uma vez
            duration: Duração da animação em milesegundos

            kwargs Opcinal
            Para poder usar fatias especificas do arquivo de sprite
            rows: row, linha, é uma sequencia horizontal de sprites
            cols: separação vertical de cada sprite
            """

A origem da sprite que estamos utilizando é no ponto 0, 0. Cada sprite individual desse arquivo tem um largura e altura de 125. 
Temos que dar um nome para ação, para posteriormente nos referirmos a ela, escolhemos "run". Cada objeto Animation pode conter várias ações de animação, tais como correr, andar, pular. Nesse caso definimos apenas uma

.. code-block:: python

    girl.create_animation(0, 0, 125, 125, "run")

Atualização da Animação
---------------
É necessário atualizar a animação no loop do pygame e determina a posição x, y. Se nenhum valor de x, y for definido será usado o valor padrão.

.. code-block:: python

    screen.blit(girl.update_surface(), (girl.x, girl.y))

E pronto, a animação está feita!

.. image:: /examples/images/showcase.gif

Esse exemplo completo está em `examples\\example1.py <https://github.com/estevaofon/pyanimation/blob/master/examples/example1.py>`_

`Parte 2 - Selecionando Animações <https://github.com/estevaofon/pyanimation/blob/master/docs/pt/tutorial-2.rst>`_
