import discord
import asyncio
from discord.ext import commands
TOKEN="ODMxNDk2NDExNTQyNTg1Mzk1.YHWFYA.k4Mp8wlKOSN9iufaUj7Vq779CXI"
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix='!', intents=intents)


@Bot.event
async def on_ready():               #Program Başlatınca Terminale Çıktı Veren Komut
    print("Antin Bot Başlatılıyor...")

@Bot.event
async def on_member_join(member): #Discord Sunucusuna Girdiğin'de Bize Mesaj verir
  channel = discord.utils.get(member.guild.text_channels, name="genel") #Mesajı Hangi Metin Kanalına Yazdıracağımız Komut
  await channel.send(f"{member}  Aramıza Hoş Geldin! :) ")
  print(f"{member} Aramıza Hoş Geldin! :) ")


@Bot.event
async def on_member_remove(member): #Discord Sunucusundan Çıktığın'da Bize Mesaj verir
  channel = discord.utils.get(member.guild.text_channels, name="genel")
  await channel.send(f"{member}  Aramızdan Ayrıldı! :( ")
  print(f"{member}  Aramızdan Ayrıldı! :( ")

@Bot.command()          
async def antin(msg):   #!antin ile alttaki mesajı verir
    await msg.send('Grup Antin Code Craft Takım 15 *Fevzi* *Beyza* *Simge*')


@Bot.command()
async def proje(msg):
    member = msg.author.mention
    await asyncio.sleep(5)   # test için 5 saniye 2400 40 dk dır
    await msg.send(member+" Deneme")
@Bot.command()
async def pmdr25dk(msg):
    member = msg.author.mention
    await asyncio.sleep(1500)
    await msg.send(member+" 25 dk ")

Bot.run(TOKEN)
