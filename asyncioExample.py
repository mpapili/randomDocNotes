#! /usr/bin/python3.6
import asyncio

async def find_divisibles(inrange, div_by):

        print(f'finding nums in range {inrange} divisible by {div_by}')
        located = []
        for i in range(inrange):
            if i % div_by == 0:
                located.append(i)
            if i % 50000 == 0:
                await asyncio.sleep(0.0001)
        print(f'done with nums in range {inrange} divisible by {div_by}')
        return(located)

async def main():
    
    divs1 = loop.create_task(find_divisibles(508000, 34113))
    divs2 = loop.create_task(find_divisibles(100052, 3210))
    divs3 = loop.create_task(find_divisibles(500, 3))

    await asyncio.wait( [divs1, divs2, divs3] ) 

    # now divs1-3 are all the return objects of the coroutines
    return(divs1, divs2, divs3)

    #print(divs1,'\n\n', divs2, '\n\n', divs3, '\n\n' )

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    divs1, divs2, divs3 = loop.run_until_complete(main())
    loop.close()
    print(divs1.result())
