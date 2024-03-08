import discord
from discord.commands import slash_command
from discord.ext import commands

class Plates(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Plates Cog is loaded!")

    @slash_command(name = "plates", description = "Get the number of plates tall at 1:38, 1:42, and 1:48 scale")
    async def plates(
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

        embed = discord.Embed(
            title=f"{length} {unit} to plates in height",
            description="Answers are approximate",
            color=discord.Colour.lighter_grey(),
        )

        embed.add_field(name="1:48 scale", value=f"{round(plates_1_48, 2)} plates", inline=True)
        embed.add_field(name="1:42 scale", value=f"{round(plates_1_42, 2)} plates", inline=True)
        embed.add_field(name="1:38 scale", value=f"{round(plates_1_38, 2)} plates", inline=True)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Plates(bot))