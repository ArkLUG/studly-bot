import discord
from discord.commands import slash_command
from discord.ext import commands

class Studs(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{type(self).__name__} Cog is loaded!")

    @slash_command(name = "studs", description = "Get the number of studs in length at 1:38, 1:42, and 1:48 scale")
    async def studs(self,
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

        embed = discord.Embed(
            title=f"{length} {unit} to studs in length",
            description="Answers are approximate",
            color=discord.Colour.lighter_grey(),
        )

        embed.add_field(name="1:48 scale", value=f"{round(studs_1_48, 2)} studs", inline=True)
        embed.add_field(name="1:42 scale", value=f"{round(studs_1_42, 2)} studs", inline=True)
        embed.add_field(name="1:38 scale", value=f"{round(studs_1_38, 2)} studs", inline=True)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Studs(bot))