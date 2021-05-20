import asyncio


async def basic_async(num):
    # the order of result is nonsequential (not depends on order, even sleeping time)
    for s in Seconds:
        r = await sleeping(*s)
        print("{0}'s {1} is finished.".format(num, r))
    return True


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_forever()
    print("Hello")