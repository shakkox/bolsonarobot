import discord
import asyncio
import random

client = discord.Client()


@client.event
async def on_ready():
    print('BOT ONLINE - Ola mundo!')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.content.lower().startswith('%musica'):
        await client.send_message(message.channel,'https://www.youtube.com/watch?v=2HnEud_VRYY')

    if message.content.lower().startswith('%mito'):
       choice = random.randint(1,2,3)
       if choice == 1:
        await client.send_message(message.channel, 'https://i.imgur.com/undefined.png')
       if choice == 2:
        await client.send_message(message.channel,"Eu sonego tudo que for possível.")
       if choice == 3:
        await client.send_message(message.channel,'https://imgur.com/YDdJeCS')


    if message.content.lower().startswith('%niobio'):
      choice = random.randint(1,2,3,4)
      if choice == 1:
        await client.send_message(message.channel,"Enéas tinha razão sobre o niobio")
      if choice == 2:
        await client.send_message(message.channel,"O nióbio vai salvar o Brasil")
      if choice == 3:
        await client.send_message(message.channel,"Terras indigenas pra que?")
      if choice == 4:
        await client.send_message(message.channel,'https://imgur.com/EmGlovQ')

    if message.content.lower().startswith('%comunismo'):
      choice = random.randint(1,2,3,4,5,6)
      if choice == 1:
        await client.send_message(message.channel,'https://imgur.com/s7eBnJ3')
      if choice == 2:
        await client.send_message(message.channel,'https://i.imgur.com/GVnkU6a.jpg')
      if choice == 3:
        await client.send_message(message.channel,'Conservadorismo veio para salvar o mundo da degeneração')
      if choice == 4:
        await client.send_message(message.channel,"esse PSOL aí é um partido de pirocas tá ok")
      if choice == 5:
        await client.send_message(message.channel,"VÁ QUEIMAR TUA ROSQUINHA QUANDO TU BEM ENTENDER PORRA")
      if choice == 6:
        await client.send_message(message.channel,"Tem que se fuder e acabou.")
      if choice == 6:
        await client.send_message(message.channel,"Nós vivemos numa ditadura gayzista")


client.run('NDA3MDA0Mjc2NTU3MjE3ODEz.DU-Oaw.isyRKKf4gLcjUjXCTvdsKq4i0EA')

