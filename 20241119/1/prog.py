def objcount(class_to_decorate):
    class DecoratedClass(class_to_decorate):
        counter = 0

        def __init__(self, *args, **kwargs):
            # Увеличиваем счётчик при создании экземпляра
            DecoratedClass.counter += 1
            super().__init__(*args, **kwargs)

        def __del__(self):
            # Уменьшаем счётчик при удалении экземпляра
            DecoratedClass.counter -= 1
            if hasattr(super(), "__del__"):
                super().__del__()

    return DecoratedClass


import sys
exec(sys.stdin.read())