import logging

import discord
from golem_garden.golems.golem import Golem

logger = logging.getLogger(__name__)


class LangChainAgentCog(discord.Cog, name="LangChainAgentCog"):

    def __init__(
            self,
    ):
        super().__init__()
        self._agent = Golem()

    async def run(
            self, ctx: discord.ApplicationContext):
        # logger.info(f"Running LangChainAgentCog...")
        await ctx.send(f"Running LangChainAgentCog... with message {ctx.message}")
        await ctx.send(self._agent.intake_message("Hello this is a test lol"))
