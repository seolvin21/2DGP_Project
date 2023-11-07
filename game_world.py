objects = [[] for _ in range(6)]
# layer 0~2: background


def add_object(o, depth = 0):
    objects[depth].append(o)


def add_objects(ol, depth = 0):
    objects[depth] += ol


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()


def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('cannot remove nonexistent object')


def clear():
    for layer in objects:
        layer.clear()
