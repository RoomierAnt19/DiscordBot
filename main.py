import nextcord
from nextcord.ext import commands
import os
from api_key import *



intents = nextcord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.members = True
buttonIndex = 0

#TOKEN = 'MTIxMzMwMDIzMjE4ODU5MjEzOA.G_Ub8O.9PYDWpWh3jl9kgdsaIDXiCBJOKj80XvWm6Fci0'

client = commands.Bot(command_prefix = '!', intents = intents)

@client.event
async def on_ready():
        await client.change_presence(status=nextcord.Status.online, activity = nextcord.CustomActivity(name= "Playing The Screams Of A Thousand Tortured Souls" ))
        print(f'{client.user} is now running!' )


initial_extensions = []

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension("cogs." +filename[:-3])


if __name__  == '__main__':
      for extention in initial_extensions:
            client.load_extension(extention)

client.run(BOTTOKEN)
