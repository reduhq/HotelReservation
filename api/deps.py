from ..db.session import db

async def get_async_db():
    async with db() as db:
        yield db