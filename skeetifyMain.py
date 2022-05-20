import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Skeetify online')


@client.event
async def on_message(message):

    if message.content.startswith('!AOTY'):
        await message.channel.send("Kendrick Lamar: Mr. Morale and the Big Steppers")



client.run('OTc3MDQzMDQ3NTMzNjQxNzI4.GsHSlG.qLPePSdAZqrehOS2Px3Uk_hqrQm0GpnkYYG4Do')