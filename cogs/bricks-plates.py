import discord
from discord.commands import slash_command
from discord.ext import commands

class BrickPlates(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"BrickPlates Cog is loaded!")

    @slash_command(name = "bp", description = "Get the number of bricks and plates tall at 1:38, 1:42, and 1:48 scales")
    async def bp(
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

        embed = discord.Embed(
            title=f"{length} {unit} to bricks and plates in height",
            description="Rounded to the nearest whole plate",
            color=discord.Colour.lighter_grey(),
        )

        embed.add_field(name="1:48 scale", value=f"{bricks_1_48} bricks and {round(plates_1_48)} plates", inline=True)
        embed.add_field(name="1:42 scale", value=f"{bricks_1_42} bricks and {round(plates_1_42)} plates", inline=True)
        embed.add_field(name="1:38 scale", value=f"{bricks_1_38} bricks and {round(plates_1_38)} plates", inline=True)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(BrickPlates(bot))