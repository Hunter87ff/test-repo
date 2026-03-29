import discord
from discord.ext import commands
from discord import app_commands

_rroles: dict[str, int] = {

}



class ReactionRole(commands.Cog):

    def __init__(self, bot : commands.Bot):
        self.bot = bot


    @app_commands.command(
        name="rrole"
    )
    @app_commands.guild_only()
    async def rrole(
        self,
        ctx : discord.Interaction,
        message_id : str,
        emoji : discord.PartialEmoji,
        role : discord.Role
    ):
        if not isinstance(ctx.channel, discord.TextChannel):
            return
        
        await ctx.response.defer(ephemeral=True)
        
        _message = await ctx.channel.fetch_message(
            int(message_id)
        )

        if _message is None:
            await ctx.followup.send(
                "Message not found !! "
            )

        await _message.add_reaction(
            emoji
        )

        _rroles[f"{message_id}-{emoji.id}"] = role.id

        await ctx.followup.send(
            "Reaction Role Added !!"
        )


    @commands.Cog.listener()
    async def on_reaction_add(reaction : discord.Reaction, user : discord.Member):
        _rrole = _rroles.get(
            f"{reaction.message.id}-{reaction.emoji.id}"
        )

        if _rrole is None:
            return

        _role = user.guild.get_role(
            _rrole
        )

        if _role is None:
            return
        
        if not user.guild.me.guild_permissions.manage_roles:
            return

        try:
            await user.add_roles(
                _role
            )

        except Exception as e:
            print(e)


    @classmethod   
    async def setup(cls, bot: commands.Bot):
        await bot.add_cog(ReactionRole(bot))


