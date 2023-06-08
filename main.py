import os
from discord.ext import commands
from datetime import date
import discord
from keep_alive import keep_alive

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')


@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def friday(ctx) -> None:
  today = date.today().weekday()
  days_until_friday = (4 - today) % 7

  messages = {
    0: "ITS FRIDAY THEEEEEEEN https://www.youtube.com/watch?v=cjgldht4PKw",
    6: "It is not Friday, my pana :(\nTodavia quedan 6 días",
    5: "It is not Friday, my pana :(\nTodavia quedan 5 días",
    4: "It is not Friday, my pana :(\nTodavia quedan 4 días",
    3: "It is not Friday, my pana :(\nTodavia quedan 3 días",
    2: "It is not Friday, my pana :(\nTodavia quedan 2 días",
    1: "Ve calentando, mi pana...",
  }

  if days_until_friday in messages:
    await ctx.channel.send(messages[days_until_friday])
  else:
    await ctx.channel.send(
      f"It is not Friday, my pana :(\nTodavia quedan {days_until_friday} días")


keep_alive()
bot.run(os.getenv('TOKEN'))
