import asyncio
from bleak import BleakClient

address = "F8:24:41:C4:96:96"

async def main():
    client = BleakClient(address)
    try:
        await client.connect()
        for service in client.services:
            print(service)
    except Exception as e:
        print(e)
    finally:
        await client.disconnect()

asyncio.run(main())
