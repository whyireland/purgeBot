import discord
import asyncio
import sys

for a in sys.argv[1:]:
    if a.startswith("token:"):
        TOKEN=str(a[6:])
        print("token:", TOKEN)
    elif a.startswith("time:"):
        try:
            time=int(a[5:])
            print("time:", time)
        except:
            print("ERROR: Time must be an int")
            input()
    elif a.startswith("playing:"):
        pStatus=a[8:]
        print("playing:", pStatus)
    else:
        print("""not recognised {}:
        --HELP--
    -ARGS-
'playing:'  |   set playing status
'time:'     |   set time to delete messages in secs
'token:'    |   bot token""".format(a))
        exit()


client=discord.Client()

@client.event
async def on_message(message):
    if message.author!=client.user:
        await client.change_presence(game=discord.Game(name=pStatus))
        await asyncio.sleep(time)
        await client.delete_message(message)
        print("deleted message!")

@client.event
async def on_ready():
    print("Logged in as: {} || {}".format(client.user.name, client.user.id))
    print("     BOT ONLINE!")


client.run(TOKEN)

#https://discordapp.com/oauth2/authorize?client_id=563430890462773263&permissions=8&scope=bot
