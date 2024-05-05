import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from nextcord import Message
from nextcord.ui import View, Button
import io
import os
from api_key import *

#Need to Fix this
class intro(Button):
    def __init__(self, name):
        super().__init__( label = name, style = nextcord.ButtonStyle.red)
     
    async def callback( self, interaction: Interaction ):
        with open('SoundBoard/Intro.txt', 'r+') as sb:
            spot = None
            sound = sb.readline()
            while sound:
                sound = sound.strip()
                if f'{interaction.user.id}' == sound:
                    spot = sb.tell()
                sound = sb.readline()
        if spot == None:
            with open('SoundBoard/Intro.txt', 'a') as sb:
                sb.write(f'{interaction.user.id}\n')
                sb.write(f'{self.label}\n')
        else:
            with open('SoundBoard/Intro.txt', 'r+') as sb:
                sb.seek(spot)
                sb.write("                                                                                                                  \n")
                sb.seek(spot)
                sb.write(f'{self.label}')



class input(commands.Cog):

    def __init__(self, client):
        self.client = client 



    @nextcord.slash_command(name = "include", description = "adds a sound to soundboard", guild_ids=[serverID])
    async def include(self, interaction: Interaction, attachment: nextcord.Attachment, name: str):
        await attachment.save(f"SoundBoard/{name}.mp3")
        await interaction.send(f"{name} has now been added to soundboard")

    @nextcord.slash_command(name = "remove", description = "removes a sound to soundboard", guild_ids=[serverID])
    async def add(self, interaction: Interaction, name: str):
        await interaction.send(f"{name} has now been removed from soundboard")
        os.remove(f'SoundBoard/{name}.mp3')


    @nextcord.slash_command(name = "intro", description = "will display Alastor's soundboard", guild_ids= [serverID])
    async def intro( self, interaction: Interaction): 
        global introName 
        introName = None
        view = View()

        for name in os.listdir("./SoundBoard"):
            if name.endswith(".mp3"):
                name = name[:-4]
                button = intro(name)
                view.add_item(button)
        
        await interaction.send("Choose an intro sound", view = view)


                

def setup(client):
    client.add_cog(input(client))