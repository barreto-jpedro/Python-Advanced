from asyncio import ensure_future
from asyncio import gather
from asyncio import get_event_loop

from aiohttp import ClientSession

NEW_DECK = "http://deckofcardsapi.com/api/deck/new"

tasks = []


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def run():
    task = []
    session = ClientSession()

    # Get new deck ID
    deck_id = (await fetch(session, NEW_DECK))["deck_id"]

    # Remove all 52 deck cards async
    for _card in range(1, 53):
        task = ensure_future(
            fetch(
                session, f"http://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1"
            )
        )

        tasks.append(task)
    responses = await gather(*tasks)

    # print what card was removed
    for resp in responses:
        print(f"Card id: {resp['cards'][0]['code']}")

    await session.close()


loop = get_event_loop()
future = ensure_future(run())
loop.run_until_complete(future)
