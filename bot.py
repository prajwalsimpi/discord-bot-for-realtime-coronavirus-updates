import os
import discord 
from dotenv import load_dotenv
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')


def to_update(argument):
    cname = argument.title()
    source = requests.get('https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/').text

    soup = BeautifulSoup(source,'lxml')

    table = soup.find('table', id="table3")
    data_dictionary = {}
    countrylist = []

    table_headers = table.tbody.find_all('tr')
    #print(table_headers)
    for tr in table_headers:
        td = tr.find_all('td')
        country = td[0].text
        countrylist.append(country)
        cases = td[1].text
        deaths = td[2].text
        data_dictionary[country] = [cases,deaths]
    res = f'Country : {cname} \nCases : {str(data_dictionary[cname][0])} \nDeaths : {str(data_dictionary[cname][1])}' 
    return res

@bot.command(help="To use update command type <!><update><space><Country Name> to get the latest cases reported in the country that you specify")
async def update(ctx, *, content: to_update):
    await ctx.send(content)

@bot.command(name = 'hello',help = 'This command can be used to check if the bot is online to respond to the requests you make')
async def online_check(ctx):
    response = f'beep boop hey there!!'
    await ctx.send(response)


bot.run(TOKEN)



""" @client.event
async def on_ready():
    '''guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)'''

    print(f'{client.user}  has connected to Discord!')#is connected to the following guild:\n'
    #f'{guild.name} (id : {guild.id})')
    #members = '\n - '.join([member.name for member in #guild.members])
    #print(f'guild members :\n - {members}')

@client.event 
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f' Hi {member.name} , welcome to my Discord Server!\nGet frequent updates on the ongoing Pandemic. Use bot commands to get latest details of Covid 19'
    )
countrylist = ['United States', 'Italy', 'Spain', 'China', 'Germany', 'France', 'Iran', 'United Kingdom', 'Switzerland', 'Belgium', 'Netherlands', 'Turkey', 'Austria', 'South Korea', 'Canada', 'Portugal', 'Brazil', 'Israel', 'Sweden', 'Australia', 'Norway', 'Czech Republic (Czechia)', 'Ireland', 'Denmark', 'Chile', 'Malaysia', 'Russia', 'Romania', 'Poland', 'Philippines', 'Ecuador', 'Japan (+Diamond Princess)', 'Luxembourg', 'Pakistan', 'Thailand', 'Saudi Arabia', 'Indonesia', 'India', 'Finland', 'Greece', 'South Africa', 'Dominican Republic', 'Iceland', 'Mexico', 'Panama', 'Peru', 'Serbia', 'Argentina', 'Singapore', 'Croatia', 'Colombia', 'Slovenia', 'Qatar', 'Estonia', 'Hong Kong', 'Algeria', 
'Egypt', 'New Zealand', 'Iraq', 'Ukraine', 'United Arab Emirates', 'Morocco', 'Lithuania', 'Armenia', 'Bahrain', 'Hungary', 'Lebanon', 'Bosnia and Herzegovina', 'Latvia', 'Moldova', 'Bulgaria', 'Slovakia', 'Tunisia', 'Andorra', 'Kazakhstan', 'Azerbaijan', 'North Macedonia', 'Costa Rica', 'Uruguay', 'Taiwan', 'Cyprus', 'Kuwait', 'Réunion', 'Jordan', 'Burkina Faso', 'Albania', 'San Marino', 'Cameroon', 'Vietnam', 'Cuba', 'Oman', 'Afghanistan', 'Ghana', 'Senegal', 'Malta', "Côte d'Ivoire", 'Uzbekistan', 'Faeroe Islands', 'Honduras', 'Channel Islands', 'Belarus', 'Mauritius', 'Nigeria', 'Sri Lanka', 'Venezuela', 'State of Palestine', 'Brunei ', 'Martinique', 'Montenegro', 'Bolivia', 'Georgia', 'Guadeloupe', 'Kyrgyzstan', 'DR Congo', 'Cambodia', 'Mayotte', 'Trinidad and Tobago', 'Kenya', 'Rwanda', 'Paraguay', 'Gibraltar', 'Liechtenstein', 'Isle of Man', 'Madagascar', 'Aruba', 'Bangladesh', 'Monaco', 'French Guiana', 'Uganda', 'Macao', 'Guatemala', 'Jamaica', 'French Polynesia', 'Togo', 'Zambia', 'Niger', 'Barbados', 'Djibouti', 'El Salvador', 'Bermuda', 'Mali', 'Guinea', 'Ethiopia', 'Tanzania', 'Maldives', 'Congo', 'Gabon', 'Sint Maarten', 'Haiti', 'New Caledonia', 'Saint Martin', 'Myanmar', 'Bahamas', 'Eritrea', 'Equatorial Guinea', 'Cayman Islands', 'Mongolia', 'Namibia', 'Saint Lucia', 'Guyana', 'Dominica', 'Curaçao', 'Syria', 'Seychelles', 'Mozambique', 'Suriname', 'Greenland', 'Laos', 'Libya', 'Eswatini', 'Benin', 'Grenada', 'Zimbabwe', 'Guinea-Bissau', 'Saint Kitts & Nevis', 'Sudan', 'Angola', 'Chad', 'Antigua and Barbuda', 'Mauritania', 'Cabo Verde', 'Turks and Caicos', 'Holy See', 'Liberia', 'Saint Barthelemy', 'Nicaragua', 'Nepal', 'Fiji', 'Montserrat', 'Somalia', 'Gambia', 'Botswana', 'Bhutan', 'British Virgin Islands', 'Central African Republic', 'Belize', 'MS Zaandam', 'Anguilla', 'Burundi', 'Caribbean Netherlands', 'Timor-Leste', 'St. Vincent & Grenadines', 'Papua New Guinea', 'Sierra Leone']

@bot.command(name=lambda countryname : countryname in countrylist)



client.run(TOKEN) """