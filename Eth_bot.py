import discord
import Eth_percentage_hourly
import time
d = Eth_percentage_hourly.Eth_price('https://www.livecoinwatch.com/')

TOKEN = 'TOKEN'
client = discord.Client()
old_price = 0
price = 0
@client.event
async def on_ready():
    channel = client.get_channel(686390614862200841)
    while True:
        if old_price > price:
            peakerwood = d.Etherium()
            price = peakerwood[4]
            await channel.send(" The currently hourly price of " + peakerwood[0] + " is " + peakerwood[4])
            old_price = price
        elif old_price < price:
            await channel.send(" The currently hourly price of " + peakerwood[0] + " is " + peakerwood[4])
        else:
            return 0
        time.sleep(1800)


client.run(TOKEN)