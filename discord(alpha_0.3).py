import discord
from discord.ext import commands
import logging
import requests
import json
import random
from covid import Covid
from datetime import datetime
import time


current_datetime = datetime.now()

covidObject = Covid()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
        
bot = commands.Bot(command_prefix='$')
bot.remove_command("help") # убираем команду хелп

@bot.group(invoke_without_command=True) # Создаем команду
async def help(ctx):
    em = discord.Embed(title = "Помощь", description = "Используйте $help <команда> что-бы узнать больше о команде", color = ctx.author.color) # Создаем ембед, тайтл заголовок, description = описание ембеда

    em.add_field(name = "Разное", value = "reverse(наоборот), flip(монетка), roll(шанс), fox(лиса), covid(ковид)") # описываем команды
    em.add_field(name = "Информация", value = "author(создатель), test(проверка)(проверка функциональности), ping(пинг), time(время)") # описываем команды

    await ctx.send(embed = em) # выводим ембед сообщением

@help.command()
async def time(ctx):

    em = discord.Embed(title = "Time", description = "Узнать время запуска бота")
    em.add_field(name = "Синтатикс", value = "$time")

    await ctx.send(embed = em)

@help.command()
async def время(ctx):

    em = discord.Embed(title = "Время", description = "Узнать время запуска бота")
    em.add_field(name = "Синтатикс", value = "$время")

    await ctx.send(embed = em)

@help.command()
async def ковид(ctx):

    em = discord.Embed(title = "Ковид", description = "Узнать информацию о Covid-19")
    em.add_field(name = "Синтатикс", value = "$ковид")

    await ctx.send(embed = em)

@help.command()
async def covid(ctx):

    em = discord.Embed(title = "Covid", description = "Узнать информацию о Covid-19")
    em.add_field(name = "Синтатикс", value = "$covid")

    await ctx.send(embed = em)


@help.command()
async def fox(ctx):

    em = discord.Embed(title = "Fox", description = "Фотка лисы")
    em.add_field(name = "Синтатикс", value = "$fox")

    await ctx.send(embed = em)

@help.command()
async def лиса(ctx):

    em = discord.Embed(title = "Лиса", description = "Фотка лисы")
    em.add_field(name = "Синтатикс", value = "$лиса")

    await ctx.send(embed = em)

@help.command()
async def пинг(ctx):

    em = discord.Embed(title = "Пинг", description = "Узнаем отклик бота")
    em.add_field(name = "Синтатикс", value = "$пинг")

    await ctx.send(embed = em)


@help.command()
async def ping(ctx):

    em = discord.Embed(title = "Ping", description = "Узнаем отклик бота")
    em.add_field(name = "Синтатикс", value = "$ping")

    await ctx.send(embed = em)



@help.command()
async def roll(ctx):

    em = discord.Embed(title = "Roll", description = "Выпадание случайного числа")
    em.add_field(name = "Синтатикс", value = "$roll <число>")

    await ctx.send(embed = em)


@help.command()
async def шанс(ctx):

    em = discord.Embed(title = "Шанс", description = "Выпадание случайного числа")
    em.add_field(name = "Синтатикс", value = "$шанс <число>")

    await ctx.send(embed = em)


@help.command()
async def flip(ctx):

    em = discord.Embed(title = "Flip", description = "Подбрасывание монетки(орел или решка)")
    em.add_field(name = "Синтатикс", value = "$flip")

    await ctx.send(embed = em)

@help.command()
async def монетка(ctx):

    em = discord.Embed(title = "Flip", description = "Подбрасывание монетки(орел или решка)")
    em.add_field(name = "Синтатикс", value = "$монетка")

    await ctx.send(embed = em)


@help.command()
async def reverse(ctx):

    em = discord.Embed(title = "Reverse", description = "Перевернуть слово")
    em.add_field(name = "Синтатикс", value = "$reverse <слово>")

    await ctx.send(embed = em)

@help.command()
async def наоборот(ctx):

    em = discord.Embed(title = "Наоборот", description = "Перевернуть слово")
    em.add_field(name = "Синтатикс", value = "$наоборот <слово>")

    await ctx.send(embed = em)   

@help.command()
async def author(ctx):

    em = discord.Embed(title = "Author", description = "Указывает автора")
    em.add_field(name = "Синтатикс", value = "$author")

    await ctx.send(embed = em)

@help.command()
async def создатель(ctx):

    em = discord.Embed(title = "Создатель", description = "Указывает автора")
    em.add_field(name = "Синтатикс", value = "$создатель")

    await ctx.send(embed = em)

@help.command()
async def test(ctx):

    em = discord.Embed(title = "Test", description = "Проверить бота")
    em.add_field(name = "Синтатикс", value = "$test")

    await ctx.send(embed = em)

@help.command()
async def проверка(ctx):

    em = discord.Embed(title = "Проверка", description = "Проверить бота")
    em.add_field(name = "Синтатикс", value = "$проверка ")

    await ctx.send(embed = em)



@bot.command()
async def test(ctx):
    author = ctx.message.author
    await ctx.send(f'Бот функционирует, {author.mention}!')

@bot.command() # 
async def проверка(ctx): 
    author = ctx.message.author 

    await ctx.send(f'Бот функционирует, {author.mention}!')
 


@bot.command()
async def author(ctx):
    author = ctx.message.author

    await ctx.send(f'Создатель:n1ght1nyou, {author.mention}!')
@bot.command() 
async def создатель(ctx):
    author = ctx.message.author

    await ctx.send(f'Создатель:n1ght1nyou, {author.mention}!') 

@bot.command() # создаём комманду
async def reverse(ctx, arg):
    author = ctx.message.author

    slovo = (arg) # применяем переменной слово = слово пользователя
    reversed_string = slovo[::-1] # переворачиваем

    await ctx.send(reversed_string) # выводим строку

@bot.command()
async def наоборот(ctx, arg):
    author = ctx.message.author

    slovo = (arg) # применяем переменной слово = слово пользователя
    reversed_string = slovo[::-1] # переворачиваем

    await ctx.send(reversed_string) # выводим строку

@bot.command()
async def flip(ctx):
    author = ctx.message.author

    flip = ['орел', 'решка', 'орел', 'решка', 'орел', 'решка', 'орел', 'решка'] # создаем список где будем хранить орел и решку
    await ctx.send(random.choice(flip)) # отправляем сообщение с рандомным выбором из списка

@bot.command()
async def монетка(ctx):
    author = ctx.message.author
    
    flip = ['орел', 'решка', 'орел', 'решка', 'орел', 'решка', 'орел', 'решка'] # создаем список где будем хранить орел и решку
    await ctx.send(random.choice(flip)) # отправляем сообщение с рандомным выбором из списка

@bot.command()
async def roll(ctx, arg):
    author = ctx.message.author

    await ctx.send(random.randint(1, int(arg)))


@bot.command()
async def шанс(ctx, arg):
    author = ctx.message.author

    await ctx.send(random.randint(1, int(arg)))

@bot.command()
async def ping(ctx):
    await ctx.send(f'Мой отклик с сервером {round (bot.latency * 1000)} ms') # Ну, тут все легко, получаем пинг от бота

@bot.command()
async def пинг(ctx):
    await ctx.send(f'Мой отклик с сервером {round (bot.latency * 1000)} ms') # Ну, тут все легко, получаем пинг от бота



@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Лисичка') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def лиса(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xff9900, title = 'Лисичка')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@bot.command()
async def boobs(ctx):
    await ctx.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@bot.group(invoke_without_command=True)
async def covid(ctx):
    covidObject.get_data()       

    confirmed = covidObject.get_total_confirmed_cases()
    active = covidObject.get_total_active_cases()
    recovered = covidObject.get_total_recovered()
    deaths = covidObject.get_total_deaths()

    em = discord.Embed(title = "Covid-19", description = "В данной таблице находится общяя информация о Covid-19", color = ctx.author.color) 
    em.add_field(name = "Зараженных", value = active)
    em.add_field(name = "Подтвержденные", value = confirmed)
    em.add_field(name = "Умерших", value = deaths) 
    em.add_field(name = "Выздоровевших", value = recovered) 

    await ctx.send(embed = em)
    await ctx.send("Не забывайте мыть руки!")

@bot.group(invoke_without_command=True)
async def ковид(ctx):
    covidObject.get_data()       

    confirmed = covidObject.get_total_confirmed_cases()
    active = covidObject.get_total_active_cases()
    recovered = covidObject.get_total_recovered()
    deaths = covidObject.get_total_deaths()

    em = discord.Embed(title = "Covid-19", description = "В данной таблице находится общяя информация о Covid-19", color = ctx.author.color) 
    em.add_field(name = "Зараженных", value = active)
    em.add_field(name = "Подтвержденные", value = confirmed)
    em.add_field(name = "Умерших", value = deaths) 
    em.add_field(name = "Выздоровевших", value = recovered) 

    await ctx.send(embed = em)
    await ctx.send("Не забывайте мыть руки!")

@bot.command()
async def time(ctx):
    em = discord.Embed(title = "Time", description = "Выводит время запуска бота", color = ctx.author.color) # Создаем ембед, тайтл заголовок, description = описание ембеда

    em.add_field(name = "Год", value = current_datetime.year)
    em.add_field(name = "Месяц", value = current_datetime.month)
    em.add_field(name = "День", value = current_datetime.day)
    em.add_field(name = "Часов", value = current_datetime.hour)
    em.add_field(name = "Минут", value = current_datetime.minute) 
    em.add_field(name = "Секунд", value = current_datetime.second)  

    await ctx.send(embed = em)

@bot.command()
async def время(ctx):
    em = discord.Embed(title = "Time", description = "Выводит время запуска бота", color = ctx.author.color) # Создаем ембед, тайтл заголовок, description = описание ембеда

    em.add_field(name = "Год", value = current_datetime.year)
    em.add_field(name = "Месяц", value = current_datetime.month)
    em.add_field(name = "День", value = current_datetime.day)
    em.add_field(name = "Часов", value = current_datetime.hour)
    em.add_field(name = "Минут", value = current_datetime.minute) 
    em.add_field(name = "Секунд", value = current_datetime.second)  

    await ctx.send(embed = em)    

bot.run('') # тут токен
