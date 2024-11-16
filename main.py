import discord
from discord.ext import commands
import requests
import pandas as pd
from bs4 import BeautifulSoup
import random
import asyncio
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print('Я готов!')

@bot.command()
async def start(ctx):
    await ctx.send('Привет!')

@bot.command()
async def calc(ctx):
    await ctx.send("Сколько кВтч электроэнергии вы используете в месяц?")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    try:
        electricity_msg = await bot.wait_for('message', check=check)
        electricity = float(electricity_msg.content)

        await ctx.send("Сколько м³ газа вы используете в месяц?")
        gas_msg = await bot.wait_for('message', check=check)
        gas = float(gas_msg.content)

        await ctx.send("Сколько километров вы проезжаете на автомобиле в месяц?")
        distance_msg = await bot.wait_for('message', check=check)
        distance = float(distance_msg.content)

        footprint = (electricity * 0.5) + (gas * 1.8) + (distance * 0.2)
        await ctx.send(f"Ваш углеродный след в месяц составляет: {footprint} кг CO2.")
    except:
        ctx.send("Ошибка")

@bot.command()
async def sov(ctx):
    sovets = (
        '''1. Сокращайте использование пластиковых изделий. Используйте многоразовые сумки и бутылки.
        2. Сортируйте мусор и утилизируйте отходы правильно.
        3. Пользуйтесь общественным транспортом, велосипедом или ходите пешком вместо использования автомобиля.
        4. Экономьте воду, не оставляйте краны открытыми и принимайте короткие души.
        5. Поддерживайте местных производителей и покупайте органические продукты.
        6. Используйте энергосберегающие лампочки и отключайте электроприборы, когда они не нужны.
        7. Участвуйте в акциях по очистке окружающей среды и высаживайте деревья.
        8. Следите за своим углеродным следом и старайтесь уменьшать его.
        9. Поддерживайте движение за защиту окружающей среды.
        10. Обучайте других о важности охраны природы и устойчивого развития.'''
    )
    await ctx.send(sovets)

@bot.command()
async def vic(ctx):
    points = 0
    await ctx.send("Вопрос: Какое газообразное вещество является основным парниковым газом? Азот/Углекислый газ/Водяной пар/Метан")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    try:
        msg = await bot.wait_for('message', check=check)

        if msg.content == 'Углекислый газ':
            await ctx.send("Правильно! 🎉")
            points += 1
        else:
            await ctx.send("Неправильно! Правильный ответ: углекислый газ.")

    except:
        await ctx.send("Ошибка!")
    await ctx.send("Какое действие считается одним из основных факторов изменения климата? Изменение солнечной активности/Лесовосстановление/Выбросы парниковых газов/Сельское хозяйство")
    def check(me):
        return me.author == ctx.author and me.channel == ctx.channel
    try:
        msg = await bot.wait_for('message', check=check)

        if msg.content == 'Лесовосстановление':
            await ctx.send("Правильно! 🎉")
            points += 1
        else:
            await ctx.send("Неправильно! Правильный ответ: лесовосстановление.")
    except:
        await ctx.send("Ошибка!")
    await ctx.send("Какое из следующих явлений является следствием глобального потепления? Увеличение числа ураганов/Увеличение числа землетрясений/Снижение уровня моря/Появление новых видов")
    def check(me):
        return me.author == ctx.author and me.channel == ctx.channel
    try:
        msg = await bot.wait_for('message', check=check)

        if msg.content == 'Увеличение числа ураганов':
            await ctx.send("Правильно! 🎉")
            points += 1
        else:
            await ctx.send("Неправильно! Правильный ответ: увеличение числа ураганов.")
    except:
        await ctx.send("Ошибка!")
    if points == 3:
        await ctx.send("**Поздравляем, вы ответили на все вопросы правильно!**")
    if points == 2:
        await ctx.send("**Вы ответили правильно на два вопроса, нужно повторить материал!**")
    if points == 1:
        await ctx.send("**Вы ответили правильно только на один вопрос, вам нужно подучить материал!**")
    if points == 0:
        await ctx.send("**Вы ответили на все вопросы неправильно. Вам нужно хорошо выучить материал!**")

@bot.command()
async def extr(ctx):
    await ctx.send(
        "*Экстренные службы:*\n"
        " - *Скорая помощь:* 103\n"
        " - *Полиция:* 102\n"
        " - *Пожарная служба:* 101\n"
        " - *Единый номер спасения:* 112\n\n"
        
        "*Советы в случае стихийных бедствий:*\n"
        " - *Будьте готовы:* Храните дома набор для выживания, включающий воду, еду, медикаменты, фонарик, радио и т.д.\n"
        " - *Соблюдайте инструкции:* Слушайте радио или телевидение, чтобы получать последние новости и инструкции от властей.\n"
        " - *Будьте осторожны:* Избегайте поврежденных зданий, проводов и других опасных объектов.\n"
        " - *Помогайте другим:* Если возможно, оказывайте помощь нуждающимся."
    )

continents = {
    "Africa": "https://www.wn.com/africa/climate-change",
    "Asia": "https://www.wn.com/asia/climate-change",
    "Europe": "https://www.wn.com/europe/climate-change",
    "North America": "https://www.wn.com/north-america/climate-change",
    "South America": "https://www.wn.com/south-america/climate-change",
    "Australia": "https://www.wn.com/australia/climate-change",
    "Antarctica": "https://www.wn.com/antarctica/climate-change" 
}

@bot.command()
async def climate(ctx):
    await ctx.send("Ищу новости о климате...")

    news_list = []
    for continent, url in continents.items():
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            article_elements = soup.find_all('h3', class_='article-title')

            if article_elements:
                article_title = article_elements[0].text.strip()
            else:
                article_title = "Не удалось найти статью."

            news_list.append(f"{continent}: {article_title}\n")

        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении данных с {continent}: {e}")
            news_list.append(f"{continent}: Не удалось найти статью.\n")

    await ctx.send("".join(news_list))
