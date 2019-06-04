import asyncio
import random
import time


async def mygen1(alist):
    while len(alist) > 0:
        c = random.randint(0, len(alist)-1)
        yield alist.pop(c)


async def mygen2(alist):
    while len(alist) > 0:
        c = len(alist) - 1
        print(alist.pop(c))
        await asyncio.wait(2)


async def waitLongTime(s):
    print("starting long wait")
    await asyncio.sleep(s)
    print("done waiting")


async def doWork():
    await mygen2(["ss"])
    await mygen2([1])
    await waitLongTime(4.0)

async def doWork1():
    op1 = mygen2(["ss"])
    await op1
    op2 = mygen2([1])
    await op2
    op3 = waitLongTime(4.0)
    await op3


async def doWork2():
    op1 = mygen2(["ss"])
    op2 = mygen2([1])
    op3 = waitLongTime(4.0)
    await asyncio.wait([op3, op2, op1])
    print("done")


async def timeout(timeInSec):
    await asyncio.sleep(timeInSec)

def getCommandAck():
    return False

async def checkForCommandAck():
    while True:
        if getCommandAck():
            break
        else:
            await asyncio.sleep(0.1)


async def issueCommandGetResponse(timeInSec):
    issueCommandViaSAL()
    timeoutTask = timeout(timeInSec)
    getAckTask = checkForCommandAck()
    await asyncio.waitAny([timeoutTask, getAckTask])
    if getAckTask.is_done:
        timeoutTask.close()
        doThingsForCompletedCommand()
    elif timeoutTask.is_done:
        getAckTask.close()
        throwTimeoutError()





if __name__ == "__main__":

    # a = ["ss", "dd", "gg"]
    # c = mygen1(a)
    # print(c)

    # strlist = ["ss", "dd", "gg"]
    # intlist = [1, 2, 5, 6]

    # strlist = ["ss"]
    # intlist = [1]

    # c1 = mygen2(strlist)
    # c2 = mygen2(intlist)
    # c3 = waitLongTime(4.0)
    # print(c1)

    # loop = asyncio.get_event_loop()
    # tasks = [c3, c1, c2]
    # loop.run_until_complete(asyncio.wait(tasks))
    # print('All jobs finished.')
    # loop.close()
    asyncio.get_event_loop().run_until_complete(doWork2())

    # asyncio.get_event_loop().run_until_complete(waitLongTime(3))
