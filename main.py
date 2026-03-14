
import discord as assemble
from discord.ext import commands

intents = assemble.Intents.all()

car = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    intents=intents
)


@car.command("say")
async def say(ctx: commands.Context, *, message: str):
    await ctx.send(message)


@car.command("embed")
async def embed(ctx : commands.Context, *, message: str):
    emb = assemble.Embed(
        title="something",
        description=message,
        color=assemble.Color.red()
    )

    await ctx.send(
        embed=emb
    )

# implement this 
@car.command()
async def userinfo(ctx: commands.Context):
    pass

# implement this 
@car.command()
async def serverinfo(ctx: commands.Context):
    pass

# implement this 
@car.command()
async def nick(ctx: commands.Context):
    pass


@car.event
async def on_ready():
    print(f"User : {car.user.name} is now online !! ") # type: ignore


# @car.event
# async def on_message(message: assemble.Message):
#     print(message.content)
#     await car.process_commands(message)



car.run("your_bot_token")

