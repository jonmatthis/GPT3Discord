import logging

import discord

logger = logging.getLogger(__name__)


class LangChainAgentCog(discord.Cog, name="LangChainAgentCog"):

    def __init__(
            self,
    ):
        super().__init__()

    async def run(
            self, ctx: discord.ApplicationContext):
        logger.info(f"Running LangChainAgentCog...")
        await ctx.send("Running LangChainAgentCog...")
