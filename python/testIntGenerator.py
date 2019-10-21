import asyncio


async def getInt(iniInt):
    await _addIntByOne(iniInt)


@asyncio.coroutine
def _wrapper(iniInt):
    yield from _addIntByOne(iniInt)


@asyncio.coroutine
def _addIntByOne(iniInt):
    while True:
        iniInt += 1
        yield iniInt


if __name__ == "__main__":

    for ii in range(10):
        print(asyncio.run(getInt(1)))

    # for ii in _wrapper(1):
    #     if ii < 10:
    #         print(ii)
    #     else:
    #         break
