import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print ('logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print ('message from {0.author} in {0.guild.name} in {0.channel}: {0.content}'.format(message))

client = MyClient()
client.run('OTU1ODM4MjI5NDY1MTY1ODM4.YjnfuA.fNfbm8wXfiF-amlJ-K8Kf6z2LoI')