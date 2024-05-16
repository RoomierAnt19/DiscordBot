import nextcord, glob, random
from nextcord import Interaction
from nextcord.ext import commands
from api_key import *
from mtgsdk import *



class mtg(commands.Cog):

    @commands.Cog.listener()
    async def on_message(self, message):
        if (message.channel.id == MTG_CHANNEL):
            if(message.author.bot == False):
                text = message.content
                firstIndex = text.find('[')
                lastIndex = text.find(']')
                if( lastIndex != -1 and firstIndex != -1 ):
                    subString = text[firstIndex + 1:lastIndex]
                    imageUrls = Card.where(name = f'{subString}').all()
                    imageUrl = imageUrls[0].image_url
                    if firstIndex == 0:
                        firstHalf = ""
                    else:
                        firstHalf = text[:(firstIndex)]
                    secondHalf = text[lastIndex + 1:]
                    await message.channel.send(f"sent by {message.author.nick} \n \"{firstHalf}[{subString}](<{imageUrl}>){secondHalf}\"")
                    await message.delete()



def setup(client):
    client.add_cog(mtg(client))