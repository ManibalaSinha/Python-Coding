
import asyncio
async def fetch():
   return "data"
async def main():
   result = await fetch()
   print(result)
asyncio.run(main())