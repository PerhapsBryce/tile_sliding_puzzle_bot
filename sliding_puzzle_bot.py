from operator import index
import discord;
from discord.ext import commands, tasks;
import random
import os #environment variable


TOKEN = os.environ['token']; #Switch to user bot token


intents = discord.Intents().all();
client = commands.Bot(command_prefix = '!', intents = intents);

template = [0,1,2,
            3,4,5,
            6,7,8]

puzzle = [0,1,2,
          3,4,5,
          6,7,8]

def swap(first, second):
    temp_value = puzzle[first];
    puzzle[first] = puzzle[second];
    puzzle[second] = temp_value;

    return;

def shuffle_puzzle():
    for i in puzzle:
        random_index = random.randrange(0,8);
        swap(i, random_index);

    return;

def stringify_puzzle():
    puzzle_string = "";

    for i in range(9):
        puzzle_string += str(puzzle[i]);
        if (i + 1) % 3 == 0:
            puzzle_string += "\n";

    return puzzle_string;

def check_puzzle():
    if puzzle == template:
        return True;
    return False;        

@tasks.loop(seconds=20)
async def change_status():
    return;


@client.event
async def on_ready():
    change_status.start();
    print('Bot ready');


@client.command (name = "play")
async def play(ctx):
    shuffle_puzzle();
    await ctx.send(stringify_puzzle());

@client.command (name = "up")
async def up(ctx):
    slide_position = puzzle.index(0);

    if slide_position < 3:
        await ctx.send("Invalid Move");
        return;

    swap(slide_position, slide_position - 3);

    if check_puzzle():
        await ctx.send("Congrats! You solved it!");
        
    await ctx.send(stringify_puzzle());

@client.command (name = "down")
async def down(ctx):
    slide_position = puzzle.index(0);

    if slide_position > 5:
        await ctx.send("Invalid Move");
        return;
    
    swap(slide_position, slide_position + 3);

    if check_puzzle():
        await ctx.send("Congrats! You solved it!");

    await ctx.send(stringify_puzzle());

@client.command (name = "left")
async def left(ctx):
    slide_position = puzzle.index(0);

    if slide_position % 3 == 0:
        await ctx.send("Invalid Move");
        return;

    swap(slide_position, slide_position - 1);

    if check_puzzle():
        await ctx.send("Congrats! You solved it!");

    await ctx.send(stringify_puzzle());

@client.command (name="right")
async def right(ctx):
    slide_position = puzzle.index(0);

    if slide_position == 2 or slide_position == 5 or slide_position == 8:
        await ctx.send("Invalid Move");
        return;

    swap(slide_position, slide_position + 1);

    if check_puzzle():
        await ctx.send("Congrats! You solved it!");

    await ctx.send(stringify_puzzle());


    

client.run(TOKEN);