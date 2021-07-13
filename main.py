# importing modules
import os
from decouple import config
import discord
import requests
import random

api = config('API')
token = config('TOKEN')

client = discord.Client()

params = {
  "q": "nicholas cage", 
  "api_key": api,
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
    lst = list(response['data'])
    gif = random.choices(lst)
    await message.channel.send(gif[0]['url'])

client.run(token)