import nextcord
from nextcord import FFmpegPCMAudio
from nextcord import Interaction
from nextcord.ext import commands
from nextcord.ui import Button, View
import os


class soundboard(Button):
    def __init__(self, name):
        super().__init__( label = name, style = nextcord.ButtonStyle.red)
     
    async def callback( self, interaction: Interaction ):
        voice = interaction.guild.voice_client
        if voice.is_playing() is False:
            source = FFmpegPCMAudio(f"SoundBoard/{self.label}.mp3")
            if interaction.guild.voice_client:
                voice = interaction.guild.voice_client
                player = voice.play(source)
            elif interaction.guild.voice_client is not interaction.user.voice.channel:
                channel = interaction.user.voice.channel
                voice = await channel.connect()
                player = voice.play(source)
            


class vc(commands.Cog):

    def __init__(self, client):
        self.client = client 

    serverID = 1213299307046903839

    
    #joins the vc you are in
    @nextcord.slash_command(name = "join", description = "Alastor will join your call", guild_ids=[serverID])
    async def join(self, interaction: Interaction):
        if(interaction.user.voice):
            channel = interaction.user.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio('ImGoingtofYou.mp3')
            #player = voice.play(source)
            await interaction.response.send_message("Done", ephemeral = True)
        else:
            await interaction.response.send_message("You are not in a voice channel, you must be in a voice channel to run this command", ephemeral = True)
    
    
    #leaves the voice channel it's in
    @nextcord.slash_command(name = "leave", description = "Alastor will leave the call", guild_ids=[serverID])
    async def leave(self, interaction: Interaction):
        if( interaction.guild.voice_client):
            await interaction.guild.voice_client.disconnect()
            await interaction.response.send_message("Done", ephemeral = True)
        else:
            await interaction.response.send_message( "I am not in a voice channel", ephemeral= True )


    #displays the soundboard
    @nextcord.slash_command(name = "soundboard", description = "will display Alastor's soundboard", guild_ids= [serverID])
    async def soundboard( self, interaction: Interaction):
        view = View()

        for name in os.listdir("./SoundBoard"):
            if name.endswith(".mp3"):
                name = name[:-4]
                button = soundboard(name)
                view.add_item(button)
        
        await interaction.send("", view = view)

    
    #Joins voice channel when you join it
    @commands.Cog.listener()
    async def on_voice_state_update( self, member, before, after ):
        if member.id != 1213300232188592138:
            # print(f'Member is in {member.voice.channel}')
            # print("---------------------------")
            # print(nextcord.VoiceClient.channel)
            # print("---------------------------")
            if before.channel is None and after.channel is not None:
                sound = "Fun"
                with open('SoundBoard/Intro.txt', 'r') as sb:
                    name = sb.readline()
                    while name:
                        name = name.strip()
                        if f'{member.id}' == name:
                            name = sb.readline()
                            sound = name.strip()
                        name = sb.readline()
                channel = after.channel
                voice = await channel.connect()
                source = FFmpegPCMAudio(f'SoundBoard/{sound}.mp3')
                player = voice.play(source)
                

    
    #pause play and stop not working but potentially don't need
    '''
    #starts to play audio file
    #needs to be updated to slash command and tested
    @commands.command( pass_context = True )
    async def play(ctx):
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio('ImGoingtofYou.mp3')
        if( voice.is_playing() == False ):
            player = voice.play(source)
        else:
            await ctx.send( "There is audio already playing" )

    '''



def setup(client):
    client.add_cog(vc(client))