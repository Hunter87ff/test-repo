import discord
from discord.ext import commands

user = commands.AutoShardedBot(
    command_prefix="naman",
    intents=discord.Intents.all()
)

@user.command(name="hello")
async def hello(ctx : commands.Context):
    await ctx.send("Hello, world!")

