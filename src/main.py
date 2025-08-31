import asyncio
import utility

from src import delete, init, login
import logging
logging.basicConfig(filename='schutzen.log', encoding='utf-8', level=logging.INFO, format="%(levelname)s:%(message)s at %(asctime)s", datefmt='%m/%d/%Y %I:%M:%S %p')

def main():
    asyncio.create_task(utility.logout())
    #init.init()
    #login.login()
    #delete.delete()

if __name__ == "__main__":
    main()
