#Tyler Dolph, Jaden Torres 2019-2020
#=======================================#
import discord
from discord.ext import commands
import random
import time
import os, os.path
from os import walk
import urllib.request
import base64
import asyncio
import re
#=======================================#
INF = 2147483647
PREFIX = '~'
client = commands.Bot(command_prefix = PREFIX)
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
#=======================================#
filestuff = ['.gif','.png','.jpg','.mov','.mp4','.mp3','.webp']
#escape_dict={'\b':r'','\c':r'','\f':r'','\n':r'','\r':r'','\t':r'','\v':r'',
 #            '\'':r'','\"':r'','\0':r'','\1':r'','\2':r'',
  #           '\3':r'','\4':r'','\5':r'','\6':r'','\7':r'','\8':r'','\9':r''}
escape_dict={'\n':r''}
memecounter = 0
#=======================================#
def raw(text):
    #gets rid of unfresh and unrad characters that we don't want
    new_string=''
    for char in text:
        try: new_string+=escape_dict[char]
        except KeyError: new_string+=char
    #new_string = new_string[:-3]
    return new_string
#=======================================#
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="my prefix is a squiggly line"))
    #await client.change_presence(activity=discord.CustomActivity(name="my prefix is a squiggly line"))
    print('Aespir is ready')

    await shuffleImages(memecounter,memelist, 'memes')
    await shuffleImages(cutecounter,cutelist, 'cute')
#=======================================#
#=======================================#
client.remove_command('help')
@client.command()
async def help(ctx): #a custom yet garbage help command
    await ctx.send('''```aespir v0.4, prefix \''''+PREFIX+''''\n---\ncommands:
ping (pong!)
flip (a coin)
8ball {your question}
echo {your message}
uwu {your text} (uwu)
meme (yes)
addmeme {media attachment or link}
cute (absolutely)
addcute {media attachment or link}
bubblewrap {custom message, defaults to pop}
hellfire {password} {custom message, defaults to something fun}
roulette (russian!)
roulettespin (spins the chamber, if you're into that sort of thing)
roulettebutwithasemiautomaticpistol (uh)
pp (nice pp)
gay {message (optional)} (gay)
pingme (pings you after a randomized timer. why would you use this?????)
whoami (for testing)
invite (yes pls)```''')
    print(f'help     {round(client.latency*1000)}ms')
#=======================================#
@client.event 
async def on_message(message):
    await client.process_commands(message)
#=======================================#
    if message.author == client.user: return
    msg = message.content.lower().replace(",","")
#=======================================# sus 
    if 'sus' in msg:
        await message.channel.send('sus!!!')
        print(f'sus      {round(client.latency*1000)}ms')
#=======================================# dad
    imList = ['i\'m ','im ','i am ']
    for im in imList:
        if im in msg:
            msgList = msg.split(im)
            if len(msgList) > 1: person = msgList[1]
            else: person = msgList[0]
            await message.channel.send('hi ' + person +', '+im+'dad!')
            print(f'imdad    {round(client.latency*1000)}ms')
            return
#=======================================#
@client.command()
async def ping(ping): #pong!
    await ping.send(f'pong! {round(client.latency*1000)}ms')
    print(f'pong!    {round(client.latency*1000)}ms')
#=======================================#
@client.command(aliases =['8ball']) #an 8ball command idk
async def _8ball(ctx,*,question):
    responses = [ 'It is certain.','It is decidedly so.','Without a doubt.','Yes - definitely.','You may rely on it.',
                  'As I see it, yes.','Most likely.','Outlook good.','Yes.','Signs point to yes.','Reply hazy, try again.',
                  'Ask again later.','Better not tell you now.','Cannot predict now.','Concentrate and ask again.',
                  'Don\'t count on it.','My reply is no.','My sources say no.','Outlook not so good.','Very doubtful.']
    await ctx.send(f'```Question: {question}\nAnswer: {random.choice(responses)}```')
    print(f'8ball    {round(client.latency*1000)}ms')
#=======================================#
@client.command() 
async def uwu(ctx,*,text):
    replaceWithW=['l','r']
    vowels = ['a','e','i','o','u']
    for letter in replaceWithW: 
        text = text.replace(letter, 'w')
        text = text.replace(letter.upper(), 'W')
    text = text.replace('ov', 'uv')
    text = text.replace('Ov', 'Uv')
    letternum = 0
    for letter in text:
        if (letter == 'n' or letter == 'N') and text[letternum+1] in vowels: text = text[0:letternum+1]+'y'+text[letternum+1:len(text)]
        letternum+=1
    await ctx.send(f'{text}')
    print(f'uwu      {round(client.latency*1000)}ms')
#=======================================#
@client.command() 
async def echo(ctx,*,text):
    await ctx.send(text)
    print(f'echo     {round(client.latency*1000)}ms')
#=======================================#
@client.command(pass_context=True) 
async def pingme(ctx):
    await ctx.send('will do!')
    print(f'pingme0  {round(client.latency*1000)}ms')
    await asyncio.sleep(random.randint(300,1200))
    await ctx.send(ctx.message.author.mention)
    print(f'pingme1  {round(client.latency*1000)}ms')
#=======================================#
@client.command()
async def bubblewrap(ctx,*,pop='pop'):
    await ctx.send(("|| "+pop+" ||") * int(2000/((len(pop)+6))))
    print(f'bwrap    {round(client.latency*1000)}ms')
#=======================================#
@client.command()
async def flip(ctx):
    coin = ['heads','tails']
    await ctx.send(f'you flipped {random.choice(coin)}!')
    print(f'flip     {round(client.latency*1000)}ms')
#=======================================#
async def shuffleImages(counter, imglist, folder):
    imglist = os.listdir(f'.\\'+folder)
    counter = 0
    random.shuffle(imglist)
    print('shuffled the '+folder)
    return(counter, imglist)
#=======================================#
memelist = []
memecounter = 0
@client.command()
async def meme(ctx): #memes yeyeye
    global memelist
    global memecounter
    if memecounter >= len(memelist)-2: 
        memecounter, memelist = await shuffleImages(memecounter,memelist, 'memes')
    memecounter = await image(ctx,memelist,memecounter,'memes','meme')
#=======================================#
cutelist = []
cutecounter = 0
@client.command()
async def cute(ctx): #kittens yeyeye
    global cutelist
    global cutecounter
    if cutecounter >= len(cutelist)-2: 
        cutecounter, cutelist = await shuffleImages(cutecounter,cutelist, 'cute')
    cutecounter = await image(ctx,cutelist,cutecounter,'cute','cute image')
#=======================================#
async def imageNum(directory):
    num = 0
    for img in os.listdir(directory):
        newNum = int(img.split('.')[0])
        if newNum > num:
            num = newNum
    return num+1
#=======================================#
@client.command() #command to add  m e m e s
async def addmeme(ctx, link = ''):
    await addimage(ctx, link, 'memes')
    print(f'addmeme  {round(client.latency*1000)}ms')
#=======================================#
@client.command() #command to add  m e m e s
async def addcute(ctx, link = ''):
    await addimage(ctx, link, 'cute')
    print(f'addcute  {round(client.latency*1000)}ms')
#=======================================#
async def image(ctx, imglist, counter, folder, word):
    sent = imglist[counter]
    await ctx.send('your '+word+', good lad',file=discord.File('.\\'+folder+'\\'+sent))
    print(f'{word.split()[0]}     {round(client.latency*1000)}ms')
    return counter + 1
#=======================================#
async def addimage(ctx, link, folder):
    global user_agent 
    headers={'User-Agent':user_agent,}
    if ctx.message.attachments: link = ctx.message.attachments[0].url
    islink = False

    if link:
        for end in filestuff:
            if end in link[len(link)-len(end):len(link)]: islink = True

    if islink:
        request=urllib.request.Request(link, None, headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        #newImg = open('.\memes\\'+(str(len(os.listdir('.\memes'))+1)+'.'+link.split('.')[-1]), "wb")
        newImg = open('.\\'+folder+'\\'+str(await imageNum('.\\'+folder))+'.'+link.split('.')[-1], "wb")
        newImg.write(data)
        newImg.close()
        await ctx.send('```your media has been added to the collection :)```')

    else: await ctx.send('```woah there buckaroo, not so fast. we only want media attachments and links in these parts, \'yahear.```')
#=======================================#
chambers = {}
@client.command(pass_context=True)
async def roulette(ctx):
    global chambers
    id = ctx.channel.id
    if id not in chambers: chambers[id]=-1
    pos = chambers[id]
    if pos < 0: pos = random.randint(0,5)
    if pos == 0: await ctx.send('```bang!```')
    else: await ctx.send('```click...```')
    chambers[id]-=1
    print(f'roulette {round(client.latency*1000)}ms')
#=======================================#
@client.command()
async def roulettespin(ctx):
    global chambers
    chambers[ctx.channel.id] = random.randint(0,5)
    await ctx.send('```haha chamber go spin```')
    print(f'spin     {round(client.latency*1000)}ms')
#=======================================#
funkytime = False
@client.command()
async def botcontrol(ctx):
    global funkytime
    while funkytime:
        msg = input()
        await ctx.send(msg)
#=======================================#
@client.command()
async def invite(ctx):
    link = 'https://discord.com/oauth2/authorize?client_id=459165488572792832&scope=bot'
    await ctx.send('```okay, here ya go! ^-^```'+link)
    print(f'invite   {round(client.latency*1000)}ms')
#=======================================#
@client.command()
async def roulettebutwithasemiautomaticpistol(ctx): 
    await ctx.send('```bang!```')
    print(f'rip lmao {round(client.latency*1000)}ms')
#=======================================#
@client.command()
async def pp(ctx, userString = None): 
    if not userString: await ctx.send('here be your pp, my good lad: 8'+('='*random.randint(1,20)+')'))
    else: await ctx.send('here be '+userString+'\'s pp, my good lad: 8'+('='*random.randint(1,20)+')'))
    print(f'pp       {round(client.latency*1000)}ms')
#=======================================#
@client.command(pass_context=True)
async def gay(ctx,*,userString = None):
    if not userString: userString = str(ctx.message.author.name)
    random.seed(userString)
    num = int(random.random()*100)
    #num = random.randint(0,101)
    #num = random.seed(ord(userString[0]))
    if num >= 95: num = 100
    if num <= 5: num = 0
    if not userString: await ctx.send('```you are '+ str(num) +'%'+ ' gay```')
    else: await ctx.send(userString + ' is ' + str(num) +'%'+ ' gay')
    #if not userString: await ctx.send('```you are '+ str(100) +'%'+ ' gay```')
    #else: await ctx.send('```'+ userString + ' is ' + str(100) +'%'+ ' gay```')
    print(f'gay      {round(client.latency*1000)}ms')
#=======================================#
@client.command(pass_context=True)
async def whoami(ctx):
    await ctx.send('you are '+ ctx.message.author.name + ", id "+ str(ctx.message.author.id))
#=======================================#
async def hellfireLoop(ctx, message):
    await ctx.send(message)
    await asyncio.sleep(5)
    print('lmao')
#=====================#
@client.command()
async def hellfire(ctx,passwordinp,*,message = 'something fun'):
    hellfile = open("hellpassword.txt","r+") #get the token from token.txt
    passwords = ''
    read_line = 'sansundertale'
    password = raw(str(hellfile.readline()))
    while read_line != '':
        read_line = raw(str(hellfile.readline()))
        passwords += read_line.replace(' ','') + '\n'
    if passwordinp == password and password != '':
        await ctx.send('```hellfire accepted. commencing...```')
        print(f'hellfire {round(client.latency*1000)}ms')
        hellfile.truncate(0)
        hellfile.seek(0)
        hellfile.write(passwords)
        hellfile.close()
        coros = [hellfireLoop(ctx,message) for _ in range(100)]
        await asyncio.gather(*coros)
    elif password == '':
        await ctx.send('```hellfire denied, no password set.```')
        hellfile.close()
        print(f'hellfire denied, no password set. set one in hellfire.txt.')
    else:
        await ctx.send('```hellfire denied.```')
        hellfile.close()
#=======================================#
tokenfile = open("token.txt","r") #get the token from token.txt
token = tokenfile.readline()
tokenfile.close()
def clientrun():
    global token
    #print('connecting with token '+token)
    print('connecting...')
    try:
        client.run(token)
    except Exception:
        input('error, most likely bad token passed. press enter to exit.')
#=======================================#
clientrun()
#=======================================#