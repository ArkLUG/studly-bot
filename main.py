import os
import discord
from dotenv import load_dotenv

load_dotenv() # load all the variables from the .env file

bot = discord.Bot()

@bot.event
async def on_ready():
    await bot.sync_commands()
    print(f"{bot.user} is ready and online!")

# Load cogs without having to hardcode them all
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.getenv('DISCORD_TOKEN')) # run the bot with the token