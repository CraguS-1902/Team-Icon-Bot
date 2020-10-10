import asyncio


import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Wir sind eingeloggt als User {}'.format(client.user.name))
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('team icøn'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('TEAM ICØN'), status=discord.Status.online)
        await asyncio.sleep(3)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if '/help' in message.content:
        await message.channel.send('**Hilfe zum PyBot**\r\n'
                                   'https://media.discordapp.net/attachments/763014669409320991/763491804406218812/Logo_Animation_11.gif?width=468&height=468')


client.run('NzY0NDIxMDcwNDY3MTA0NzY4.X4GAmQ.NRFKJynAKaAIf8AQ_lBl4dY3FXc')
