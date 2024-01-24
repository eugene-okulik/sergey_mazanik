"""
Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция
Код, использующий этот декоратор может выглядеть, например, так:
@repeat_me
def example(text):
    print(text)
example('print me', count=2)
В результате работы будет такое:
print me
print me
Если есть время и желание погуглить и повозиться, то можно попробовать создать декоратор, который сможет обработать
такой код:
@repeat_me(count=2)
def example(text):
    print(text)
example('print me')
"""

# --------------------- 1nd version ---------------------


def repeat_me(func):
    def wrapper(*args, **kwargs):
        for i in range(kwargs['count']):
            func(*args)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)


# --------------------- 2nd version ---------------------


def repeat_me(**kwargs):
    def decor(func):
        def wrapper(*args):
            for i in range(kwargs['count']):
                func(*args)

        return wrapper

    return decor


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
