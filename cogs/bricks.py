import discord
from discord.commands import slash_command
from discord.ext import commands

class Bricks(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{type(self).__name__} Cog is loaded!")

    @slash_command(name = "bricks", description = "Get the number of bricks tall at 1:38, 1:42, and 1:48 scale")
    async def bricks(
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

        embed = discord.Embed(
            title=f"{length} {unit} to bricks in height",
            description="Answers are approximate",
            color=discord.Colour.lighter_grey(),
        )

        embed.add_field(name="1:48 scale", value=f"{round(bricks_1_48, 2)} bricks", inline=True)
        embed.add_field(name="1:42 scale", value=f"{round(bricks_1_42, 2)} bricks", inline=True)
        embed.add_field(name="1:38 scale", value=f"{round(bricks_1_38, 2)} bricks", inline=True)
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Bricks(bot))