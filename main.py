import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive
import os

prefix = "$$"

keep_alive()
token = os.getenv("token")

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.offline)
    print("{0.user} is ready!".format(bot))

@bot.command()
async def stopbump(ctx):
  await ctx.send("Stopping in 5 seconds")
  await asyncio.sleep(5)
  global dmcs
  dmcs=False
  await ctx.send("Done 👍")

  
  

@bot.command()
async def helpdank(ctx):
    await ctx.message.delete()
    await ctx.send('$$AutoDank: Pls beg, Pls dig, Pls fish, pls hunt, dep all. $$StopAutoDank: Stops the bot.')

@bot.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send('$$AutoDank: Pls beg, Pls dig, Pls fish, pls hunt, dep all. $$StopAutoDank: Stops the bot.')

@bot.command()
async def stopautodank(ctx):
    await ctx.message.delete()
    await ctx.send('AutoDank is now Disabled :blush: to enable it again rerun the replit')
    await bot.close()
    
  
@bot.command(pass_context=True)
async def autodank(ctx):
    await ctx.message.delete()
    await ctx.send('AutoDank is now Enabled :blush:')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(5)
            await ctx.send('pls beg')
            print(f"{Fore.GREEN}succefully sent pls beg")
            await asyncio.sleep(1)
            await ctx.send('pls fish')
            print(f"{Fore.GREEN}succefully sent pls fish")
            await asyncio.sleep(1)
            await ctx.send('pls dig')
            print(f"{Fore.GREEN}succefully sent pls dig")
            await asyncio.sleep(1)
            await ctx.send('pls hunt')
            print(f"{Fore.GREEN}succefully sent pls hunt")
            await asyncio.sleep(1)
            await ctx.send('pls dep all')
            print(f"{Fore.GREEN}succefully sent pls dep all")
            await asyncio.sleep(34)
            await ctx.send('pls fish')
            print(f"{Fore.GREEN}succefully sent pls fish")
            await asyncio.sleep(1)
            await ctx.send('pls dig')
            print(f"{Fore.GREEN}succefully sent pls dig")
            await asyncio.sleep(1)
            await ctx.send('pls hunt')
            print(f"{Fore.GREEN}succefully sent pls hunt")
            await ctx.send('pls dep all')
            print(f"{Fore.GREEN}succefully sent pls dep all")
            await asyncio.sleep(1)
            await ctx.send('pls beg')
            print(f"{Fore.GREEN}succefully sent pls beg")
            await asyncio.sleep(39)
           

keep_alive()
bot.run(os.getenv('token'),  bot=False)
