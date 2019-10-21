import logging


def fab(maxVal):
    n, a, b = 0, 0, 1
    while (n < maxVal):
        yield b

        a, b = b, a + b
        n = n + 1


def f_wrapper(fun_iterable):
    print('start')
    for item in fun_iterable:
        yield item

    print('end')


def f_wrapper2(fun_iterable):
    print('start')
    yield from fun_iterable
    print('end')


if __name__ == "__main__":
    wrap = f_wrapper2(fab(5))
    for ii in wrap:
        print(ii, end=" ")
