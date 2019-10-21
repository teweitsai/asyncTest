import asyncio
import time


async def countWrapper():
    await count()


async def count():
    print("One")
    # await asyncio.sleep(3)
    # await sleepAndPrint()
    # sleepAndPrint()
    time.sleep(3)
    print("Two")


async def sleepAndPrint():
    print("Begin sleep.")
    await asyncio.sleep(1)
    print("Finish sleep.")


async def main():
    await asyncio.gather(countWrapper(), countWrapper(), countWrapper())


if __name__ == "__main__":

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
