import discord
import asyncio
from discord.ext import commands
TOKEN="ODMxNDk2NDExNTQyNTg1Mzk1.YHWFYA.XVEijfOaROyR3gYUnYXz2l0-wKM"
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix='!', intents=intents)


@Bot.event
async def on_ready():               #Program Başlatınca Terminale Çıktı Veren Komut
    print("Antin Bot Başlatılıyor...")

@Bot.event
async def on_member_join(member): #Discord Sunucusuna Girdiğin Bize Mesaj verir
  channel = discord.utils.get(member.guild.text_channels, name="genel") #Mesajı Hangi Metin Kanalına Yazdıracağımız Komut
  await channel.send(f"{member}  Aramıza Hoş Geldin! :) ")
  print(f"{member} Aramıza Hoş Geldin! :) ")


@Bot.event
async def on_member_remove(member):
  channel = discord.utils.get(member.guild.text_channels, name="genel")
  await channel.send(f"{member}  Aramızdan Ayrıldı! :( ")
  print(f"{member}  Aramızdan Ayrıldı! :( ")

@Bot.command()
async def antin(msg):
    await msg.send('Grup Antin Code Craft Takım 15 *Fevzi* *Beyza* *Simge*')


@Bot.command()
async def antin2(msg):
    member = msg.author.mention
    await asyncio.sleep(5)
    await msg.send(member+" 5 saniye")
@Bot.command()
async def pmdr25dk(msg):
    member = msg.author.mention
    await asyncio.sleep(1500)
    await msg.send(member+" 40")
@Bot.command()
async def antin4(msg):
    member = msg.author.mention
    await asyncio.sleep(5)
    await msg.send(member+" 40")
@Bot.command()
async def antin5(msg):
    member = msg.author.mention
    await asyncio.sleep(5)
    await msg.send(member+" 40")

Bot.run(TOKEN)
