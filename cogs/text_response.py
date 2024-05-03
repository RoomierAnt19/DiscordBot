import nextcord
from nextcord import Interaction
from nextcord.ext import commands



class text_responce(commands.Cog):

    def __init__(self, client):
        self.client = client 

    serverID = 1213299307046903839


    #Random Responces
    @commands.Cog.listener()
    async def on_message(client, message):
        if (message.author != Interaction.user):
            if ("reddit" in message.content.lower()):
                await message.reply("", file = nextcord.File('opinion.gif'))
            elif (f'<@1213300232188592138>' in message.content.lower()):
                await message.reply("Do you mind? I'm in the middle of breakfast.")


    @nextcord.slash_command(name = "hello", description = "Say hello to Alastor", guild_ids=[serverID])
    async def hello(self, interaction: Interaction):
        await interaction.response.send_message("Hello there")

    
    @nextcord.slash_command(name = "opinion", description = "Your opinion", guild_ids = [serverID])
    async def opinion( self, interaction: Interaction):
        await interaction.send(file=nextcord.File('opinion.gif'))
    


def setup(client):
    client.add_cog(text_responce(client))