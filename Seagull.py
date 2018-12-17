import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


TOKEN = 'NTI0MDY2MjQ5Mzk1OTI5MTAz.Dviq5A.2sixszdetiEQW56lf4AvS2HxTEs'

bot = commands.Bot(command_prefix = '-') 
status = ['test3', 'test1', '.test']

@bot.event
async def on_ready():
    print('Seagull is ready to fly')

@bot.event
async def on_message(message):
 author = message.author
 content = message.content
 print ('{}: {}'.format(author, content))

@bot.command(pass_context=True)
async def ban(ctx, member: discord.Member):
    await bot.ban(member)
    await bot.say('Banned {0}'.format(member.mention))
    


    
bot.loop.create_task(change_status())
bot.run(TOKEN)    
