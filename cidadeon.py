import discord
from discord import app_commands
from discord.ext import commands

class CidadeOn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Slash command
    @app_commands.command(
        name="cidadeon",
        description="Envia a embed de Cidade On do Balneário Roleplay."
    )
    async def cidadeon_slash(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="A Cidade esta On venha fazer seu Roleplay no Balneário Roleplay!🏖️",
            description="**Em Balneário Roleplay, você poderá ter:**\n \n **(💸) Drops, de armas, joias, etc...**\n **(💼) Podes trabalhar de tudo!**\n **(🎉) Sorteios e eventos!**\n **(❓) E MAIS!**\n\n**__🐚 Server Info:__**\n\n**🌴 Fundadores:** <@1227688679313768518> e <@1376364655894859816>\n**🏄 Código:** hi164p38 \n https://www.roblox.com/games/start?placeId=7711635737&launchData=joinCode%3Dhi164p38\n<@&1462515697635561634>",
            color=discord.Color.from_rgb(255, 255, 255)
        )

        embed.set_image(url="https://media.discordapp.net/attachments/1462540495858172106/1463560411604320380/image.png")

        await interaction.response.send_message(embed=embed)

    # Comando com prefixo (!cidadeon)
    @commands.command(name="cidadeon")
    async def cidadeon_prefix(self, ctx):
        embed = discord.Embed(
            title="A Cidade esta On venha fazer seu Roleplay no Balneário Roleplay!🏖️",
            description="**Em Balneário Roleplay, você poderá ter:**\n \n **(💸) Drops, de armas, joias, etc...**\n **(💼) Podes trabalhar de tudo!**\n **(🎉) Sorteios e eventos!**\n **(❓) E MAIS!**\n\n**__🐚 Server Info:__**\n\n**🌴 Fundadores:** <@1227688679313768518> e <@1376364655894859816>\n**🏄 Código:** hi164p38 \n https://www.roblox.com/games/start?placeId=7711635737&launchData=joinCode%3Dhi164p38\n<@&1462515697635561634>",
            color=discord.Color.from_rgb(255, 255, 255)
        )

        embed.set_image(url="https://media.discordapp.net/attachments/1462540495858172106/1463560411604320380/image.png")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(CidadeOn(bot))
