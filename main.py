import os
import discord
import requests
import random

api_key = os.environ['API']
my_token = os.environ['TOKEN']
my_gif = ''

client = discord.Client()
params = {
  "q": "nicholas cage", 
  "api_key": api_key,
  "limit": 10,
  "lang": "en"
}
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('Cage Me!'):
    response = requests.get("http://api.giphy.com/v1/gifs/search", params=params).json()
    for r in response['data']:
      #gif = random.choices(r['url'])
      print(r['url'])
      await message.channel.send(r['url'])

client.run(my_token)