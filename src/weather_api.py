import httpx


async def fetch_url(url, params):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        return response.json()
