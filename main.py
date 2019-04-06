import discord
import asyncio

# put your bot's token here VV
TOKEN = "Put your bot's token here :)"

# a = time till messages get deleted
a = 1600


client=discord.Client()

@client.event
async def on_message(message):
    if message.author!=client.user:
        await client.change_presence(game=discord.Game(name="Deleting old messages! || "))
        await asyncio.sleep(a)
        #await client.send_message(client.get_channel("563447331844915220"), "```\n     BOT-LOG\n-----------------\n|deleted message|\n-----------------```{}\n\n{}\n\n{}".format(message.content)
        await client.delete_message(message)
        print("deleted message!")

@client.event
async def on_ready():
    print("Logged in as: {} || {}".format(client.user.name, client.user.id))


if TOKEN != "Put your bot's token here :) ":
    client.run(TOKEN)
else:
    print("Cheange the 'TOKEN' variable!")

#https://discordapp.com/oauth2/authorize?client_id=563430890462773263&permissions=8&scope=bot
