import discord
import os
import datetime
from datetime import date
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!friday'):
      today = date.today().weekday()
      #friday = today + datetime.timedelta((4-today.weekday())%7)
      #f = today - datetime.timedelta(friday)
      #f = f.strftime("%d %H %M")
      if today == 4:
        await message.channel.send('ITS FRIDAY THEEEEEEEN https://www.youtube.com/watch?v=cjgldht4PKw') 
      elif today == 5: 
        await message.channel.send('It is not Friday, my pana :(')
        await message.channel.send('Todavia quedan 6 días')
      elif today == 6: 
        await message.channel.send('It is not Friday, my pana :(')
        await message.channel.send('Todavia quedan 5 días')
      elif today == 3: 
        await message.channel.send('Ve calentando, mi pana...')
      else: 
        fridays = 4 - today%4
        await message.channel.send('It is not Friday, my pana :(')
        await message.channel.send('Todavia quedan '+ str(fridays) + "días")

keep_alive()
client.run(os.getenv('TOKEN'))