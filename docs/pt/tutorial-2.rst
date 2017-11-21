Selecionando Animações
===========
Vamos agora criar algumas animações com o persongem Link

.. raw:: html

    <img src="/examples/images/link.png" width="400px">

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


Esse arquivo contém várias animações diferentes, por exemplo andar para frente, andar de lado. E cada ação está contida em uma linha separada.
Vamos fazer a animação do personagem andar olhando para o jogador. A origem da ação está no ponto 0, 525, o comprimeto da sprite é de 121, e sua altura é de 132. Nomearemos essa ação de "front". Precisamos ajustar o valor da duração para 90, caso contrário a animação fica muito rápida.
E como dissemos cada ação está contida em uma linha, por isso utilizamos o parametro rows=1, para realizar esse fatiamento.

Para montar a animação com o personagem andando de costas para o jogador os mesmos passos acima são realizados, e o nome dado é "back. Assim, criamos duas animações diferentes para o link. 

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

O exemplo completo se encontra em `examples\\example4.py <https://github.com/estevaofon/pyanimation/blob/master/examples/example4.py>`_

`Parte 3 - Criando Animações com sprites desorganizadas <https://github.com/estevaofon/pyanimation/blob/master/docs/pt/tutorial-3.rst>`_
