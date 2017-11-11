Pyanimation
===========
A python module to easily create animations in pygame

![Alt text](/examples/images/spritesheet.png?raw=true "mini-dbz")

![Alt text](/examples/images/showcase.gif?raw=true "mini-dbz")

Setup
-----
```bash
    $ pip install pygame pyanimation
```

Cose sample
-----
```python
girl = Animation("images/spritesheet.png")
girl.create_animation(0, 0, 125, 125, 4, "run", duration=50, rows=4)
screen.blit(girl.update_surface(), (girl.x, girl.y))
```
Look in the examples for a complete example code.
