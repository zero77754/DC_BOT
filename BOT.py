import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print("Bot is online~")

bot.run('NzY1MDM5NjQ5MTIxODk0NDUx.X4PAsg.IsYvRZzDqAoC1HW-3EGyvuDnPLc')
