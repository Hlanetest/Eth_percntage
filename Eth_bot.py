import discord
import Eth_percentage_hourly
import time

d = Eth_percentage_hourly.Eth_price('https://www.livecoinwatch.com/')

TOKEN = 'TOKEN'
client = discord.Client()
@client.event
async def on_ready():
    price = int(0)
    print('1')
    old_price = float(0)
    print('2')
    channel = client.get_channel(686390614862200841)
    print('3')
    while True:
        print('Now we loop!')
        peakerwood = d.Etherium()
        price = float(peakerwood[4].replace('$', ''))
        per = int(0)
        if price >= old_price:
            print('I am here again')
            if old_price == 0:
                await channel.send("The current price of " + peakerwood[0] + " is " + peakerwood[4])
                print('Ima loop')
                old_price = price
                print('I got dat $$$')
            elif price == old_price:
                await channel.send("The current price of " + peakerwood[0]+ " Has remained the same at " + peakerwood[4])
                old_price = price

            else:
                per = int(price - old_price)
                per_total = float(per / old_price * 100)
                await channel.send(" The currently hourly price of "+ peakerwood[0]+" has gone up to "+ peakerwood[4]+ ' '  + per_total)
                old_price = price
            
            
        elif price < old_price:
            per = int(old_price - price)
            print (price)
            per_total = float(per / old_price * 100)
            print(old_price)
            await channel.send("The currently hourly price of " + peakerwood[0] + " has gone down to " + peakerwood[4] + " It has decreased to " + per_total)
        else:
            return 0
        time.sleep(300)


client.run(TOKEN)