import os
from xml.dom.minidom import Element
import discord
from dotenv import load_dotenv
from discord.ext import commands
from userData import User

#get token + guild name
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

### GAME STUFF ###

#Lists for indiv balances
#users(userID, balance, workMoney, promoBonus, timeRequiredPromo, timeUntilPromo)

# userID = 0
# balance = 1
# workMoney = 2
# promoBonus = 3
# timeRequiredPromo = 4
# timeUntilPromo = 5 

users = []


def findUser(userID):
    for user in users:
        if (user.userID == userID):
            return user
    return None
            


## COMBAT
mobs = []
# mob name = ['mob name' , health , damage , defense , mob type] add true damage?
zombie = ['zombie' , 150 , 50, 0, 'undead']

### BOT STUFF ###

#bot prefix

bot = commands.Bot(command_prefix=',')

#check to see of bot connects to guild
@bot.event
async def on_ready():

    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

### COMMANDS ###
#work command

@bot.command(name='work', help= '- Work for some money!')
async def work(ctx):

    #userList = list(users)

    user = findUser(ctx.author)
    if(user == None):
        user = User(ctx.author, 0, 100, 100, 10, 0)
        users.append(user)
      
   
    if (user.timeUntilPromo == user.timeRequiredPromo):
        promotedWorkMoney = user.workMoney + user.promoBonus
        user.workMoney = promotedWorkMoney
        user.balance = user.balance + user.workMoney
        user.timeUntilPromo = 0 
        await ctx.send('You got promoted! Your new salary is ' + str(promotedWorkMoney) + ' per hour')
        await ctx.send('You worked for an hour and got ' + str(user.workMoney) + ' dollars')
  
    else:
        user.timeUntilPromo = user.timeUntilPromo + 1
        user.balance = user.balance + user.workMoney
        await ctx.send('You worked for an hour and got ' + str(user.workMoney) + ' dollars')

#balance command
@bot.command(name='bal', help= '- Shows your current balance')
async def bal(ctx):

    user = findUser(ctx.author)

    if (user == None):
        bal = 0
    else:
        bal = user.balance

    await ctx.send("You have " + str(bal) + ' dollars')
        
    
bot.run(TOKEN)
