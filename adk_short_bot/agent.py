from google.adk.agents import Agent

from adk_short_bot.prompt import ROOT_AGENT_INSTRUCTION
from adk_short_bot.tools import count_characters

# This is the root agent that will be used to create the deployment GN 25 Nov 2025
root_agent = Agent(
    name="adk_short_bot",
    model="gemini-2.0-flash",
    description="A bot that shortens messages while maintaining their core meaning",
    instruction=ROOT_AGENT_INSTRUCTION,
    tools=[count_characters],
)
