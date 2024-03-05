import discord
import os # default module
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

@bot.event
async def on_ready():
    await bot.sync_commands()
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "studs", description = "Get the number of studs at 1:38, 1:42, and 1:48 scale")
async def studs(
    ctx: discord.ApplicationContext,
    length: discord.Option(int),
    unit: discord.Option(str, choices=['feet', 'meters'])):

    if (length == "feet"):
        studs_1_38 = length * 1
        studs_1_42 = length * (1 / 1.111111111111111111)
        studs_1_48 = length * (1 / 1.25)
    else:
        studs_1_38 = length * (1000 / 304.8)
        studs_1_42 = length * (1000 / 304.8 / 1.111111111111111111)
        studs_1_48 = length * (1000 / 304.8 / 1.25)

    studs_1_38 = (studs_1_38 * 100) / 100
    studs_1_42 = (studs_1_42 * 100) / 100
    studs_1_48 = (studs_1_48 * 100) / 100

    await ctx.respond(
        f"""Answers are approximate:
    {length} {unit} at 1:48 is {round(studs_1_48, 2)} studs.
    {length} {unit} at 1:42 is {round(studs_1_42, 2)} studs.
    {length} {unit} at 1:38 is {round(studs_1_38, 2)} studs."""
    )

@bot.slash_command(name = "plates", description = "Get the number of plates at 1:38, 1:42, and 1:48 scale")
async def studs(
    ctx: discord.ApplicationContext,
    length: discord.Option(int),
    unit: discord.Option(str, choices=['feet', 'meters'])):

    if (length == "feet"):
        plates_1_38 = length * (1 * 2.5)
        plates_1_42 = length * (1 / 1.111111111111111111 * 2.5)
        plates_1_48 = length * (1 / 1.25 * 2.5)
    else:
        plates_1_38 = length * (1000 / 304.8 * 2.5)
        plates_1_42 = length * (1000 / 304.8 / 1.111111111111111111 * 2.5)
        plates_1_48 = length * (1000 / 304.8 / 1.25 * 2.5)

    plates_1_38 = (plates_1_38 * 100) / 100
    plates_1_42 = (plates_1_42 * 100) / 100
    plates_1_48 = (plates_1_48 * 100) / 100

    await ctx.respond(
        f"""Answers are approximate:
    {length} {unit} at 1:48 is {round(plates_1_48, 2)} plates.
    {length} {unit} at 1:42 is {round(plates_1_42, 2)} plates.
    {length} {unit} at 1:38 is {round(plates_1_38, 2)} plates."""
    )

@bot.slash_command(name = "bricks", description = "Get the number of bricks at 1:38, 1:42, and 1:48 scale")
async def studs(
    ctx: discord.ApplicationContext,
    length: discord.Option(int),
    unit: discord.Option(str, choices=['feet', 'meters'])):

    if (length == "feet"):
        bricks_1_38 = length * (1 * 2.5 / 3)
        bricks_1_42 = length * (1 / 1.111111111111111111 * 2.5 / 3)
        bricks_1_48 = length * (1 / 1.25 * 2.5 / 3)
    else:
        bricks_1_38 = length * (1000 / 304.8 * 2.5 / 3)
        bricks_1_42 = length * (1000 / 304.8 / 1.111111111111111111 * 2.5 / 3)
        bricks_1_48 = length * (1000 / 304.8 / 1.25 * 2.5 / 3)

    bricks_1_38 = (bricks_1_38 * 100) / 100
    bricks_1_42 = (bricks_1_42 * 100) / 100
    bricks_1_48 = (bricks_1_48 * 100) / 100

    await ctx.respond(
        f"""Answers are approximate:
    {length} {unit} at 1:48 is {round(bricks_1_48, 2)} bricks.
    {length} {unit} at 1:42 is {round(bricks_1_42, 2)} bricks.
    {length} {unit} at 1:38 is {round(bricks_1_38, 2)} bricks."""
    )

@bot.slash_command(name = "bp", description = "Get the number of bricks and plates at 1:38, 1:42, and 1:48 scales")
async def studs(
    ctx: discord.ApplicationContext,
    length: discord.Option(int),
    unit: discord.Option(str, choices=['feet', 'meters'])):

    if (length == "feet"):
        bp_1_38 = length * (1 * 2.5 / 3)
        bp_1_42 = length * (1 / 1.111111111111111111 * 2.5 / 3)
        bp_1_48 = length * (1 / 1.25 * 2.5 / 3)
    else:
        bp_1_38 = length * (1000 / 304.8 * 2.5 / 3)
        bp_1_42 = length * (1000 / 304.8 / 1.111111111111111111 * 2.5 / 3)
        bp_1_48 = length * (1000 / 304.8 / 1.25 * 2.5 / 3)

    plates_1_38 = (bp_1_38 * 3) % 3
    plates_1_42 = (bp_1_42 * 3) % 3
    plates_1_48 = (bp_1_48 * 3) % 3
    bricks_1_38 = round(bp_1_38)
    bricks_1_42 = round(bp_1_42)
    bricks_1_48 = round(bp_1_48)


    await ctx.respond(
        f"""Answers are approximate:
        {length} {unit} at 1:48 is {bricks_1_48} bricks and {round(plates_1_48, 2)} plates.
        {length} {unit} at 1:42 is {bricks_1_42} bricks and {round(plates_1_42, 2)} plates.
        {length} {unit} at 1:38 is {bricks_1_38} bricks and {round(plates_1_38, 2)} plates."""
    )

bot.run(os.getenv('DISCORD_TOKEN')) # run the bot with the token