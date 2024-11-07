import json
import asyncio
import os

from kwork import Kwork
from dotenv import load_dotenv


load_dotenv()


async def main():
    api = Kwork(login=os.getenv('LOGIN'), password=os.getenv('PASSWORD'))
    projects = await api.get_projects(categories_ids=[11])

    with open('projects.json', 'w') as file:
        json.dump(projects, file, indent=4, ensure_ascii=False)

    await api.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
