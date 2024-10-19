import httpx


async def fetch_url(url, params):
    """
    Создаёт GET запрос к удаленному серверу.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        return response.json()
