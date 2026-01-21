import discord
from discord.ext import commands
import os

TOKEN = "MTQ2MzI1Njc2MjI0MDIwODk2OA.G8nEzr.jebHJodUCwPhmk9D21WKYYXL4EORv7q2bd78dg"

class MeuBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all(),
            application_id=1463256762240208968
        )

    async def setup_hook(self):
        # Carrega todos os cogs automaticamente
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                await self.load_extension(f"cogs.{file[:-3]}")

        # Sincroniza os slash commands
        await self.tree.sync()
        print("Slash commands sincronizados.")

bot = MeuBot()

bot.run("MTQ2MzI1Njc2MjI0MDIwODk2OA.G8nEzr.jebHJodUCwPhmk9D21WKYYXL4EORv7q2bd78dg")
