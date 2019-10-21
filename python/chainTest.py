import asyncio
import time


async def part1(waitTime):
    await asyncio.sleep(waitTime)
    print("Finish part1")


async def part2(waitTime):
    await asyncio.sleep(waitTime)
    print("Finish part2")


async def chain(waitTime1, waitTime2):
    start = time.perf_counter()

    print("Enter chain")

    await part1(waitTime1)
    await part2(waitTime2)
    useTime = time.perf_counter() - start
    print("Finish chain, time is %.2f." % useTime)


async def main():
    await asyncio.gather(chain(2, 3), chain(4, 3), chain(1, 3))


if __name__ == "__main__":
    # asyncio.run(chain(2, 3))

    start = time.perf_counter()
    asyncio.run(main())
    useTime = time.perf_counter() - start
    print("Total time is %.2f." % useTime)
