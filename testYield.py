from random import randint


def mygen(alist):
    while len(alist) > 0:
        c = randint(0, len(alist)-1)
        yield alist.pop(c)


def gen():
    value = "Test begins."
    while True:
        receive = yield value
        if (receive == "e"):
            print("Stop the iteration.")
            break
        value = "got: '%s'." % receive


if __name__ == "__main__":

    # a = ["aa", "bb", "cc"]
    # c = mygen(a)
    # print(c)

    g = gen()
    print(g.send(None))
    print(g.send('hello'))
    print(g.send(123456))
    # print(g.send('e'))
