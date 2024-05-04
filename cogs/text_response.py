import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from api_key import *



class text_responce(commands.Cog):

    def __init__(self, client):
        self.client = client 


    #Random Responces
    @commands.Cog.listener()
    async def on_message(self, message):
        if (message.author != Interaction.user):
            if ("reddit" in message.content.lower()):
                await message.reply("", file = nextcord.File('images/Reaction/Adam4.gif'))
            elif (f'<@1213300232188592138>' in message.content.lower()):
                await message.reply("Do you mind? I'm in the middle of breakfast.")
            elif ("based" in message.content.lower()):
                await message.reply("", file = nextcord.File('images/Misc/Based.jpg'))
            elif ("?" in message.content.lower()):
                await message.reply("", file = nextcord.File('images/Reaction/NOOO.jpg'))


    @nextcord.slash_command(name = "hello", description = "Say hello to Alastor", guild_ids=[serverID])
    async def hello(self, interaction: Interaction):
        await interaction.response.send_message("Hello there")

    
    @nextcord.slash_command(name = "opinion", description = "Your opinion", guild_ids = [serverID])
    async def opinion( self, interaction: Interaction):
        await interaction.send(file=nextcord.File('opinion.gif'))

    #When the annoying user that keeps randomly rejoining rejoins
    @commands.Cog.listener()
    async def on_member_join(self, member):
        problem = False
        guildName = self.client.guilds[0]
        with open('AnnoyingUsers.txt', 'r') as members:
            user = members.readline()
            while user:
                user = user.strip()
                if f'{member.id}' == user:
                    problem = True
                    await self.client.get_channel(CHANNEL).send(f"{member.mention} has attempted to rejoin the server again", file = nextcord.File('images/Reaction/Nuh_uh.png'))
                    await member.kick()

                user = members.readline()
        if ( problem == False ):
            await self.client.get_channel(CHANNEL).send(f"{member.mention} has join {guildName}! \n Welcome!")



def setup(client):
    client.add_cog(text_responce(client))