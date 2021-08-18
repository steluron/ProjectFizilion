# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for having some fun with people. """

import time
from asyncio import sleep
from collections import deque
from random import choice, getrandbits, randint
from re import sub

import requests
import random
from cowpy import cow

from userbot import CMD_HELP, LOGS
from userbot.events import register
from userbot.modules.admin import get_user_from_event

# ================= CONSTANT =================
METOOSTR = [
    "Me too thanks",
    "Haha yes, me too",
    "Same lol",
    "Me irl",
    "Same here",
    "Haha yes",
    "Me rn",
]

ZALG_LIST = [
    [
        "̖",
        " ̗",
        " ̘",
        " ̙",
        " ̜",
        " ̝",
        " ̞",
        " ̟",
        " ̠",
        " ̤",
        " ̥",
        " ̦",
        " ̩",
        " ̪",
        " ̫",
        " ̬",
        " ̭",
        " ̮",
        " ̯",
        " ̰",
        " ̱",
        " ̲",
        " ̳",
        " ̹",
        " ̺",
        " ̻",
        " ̼",
        " ͅ",
        " ͇",
        " ͈",
        " ͉",
        " ͍",
        " ͎",
        " ͓",
        " ͔",
        " ͕",
        " ͖",
        " ͙",
        " ͚",
        " ",
    ],
    [
        " ̍",
        " ̎",
        " ̄",
        " ̅",
        " ̿",
        " ̑",
        " ̆",
        " ̐",
        " ͒",
        " ͗",
        " ͑",
        " ̇",
        " ̈",
        " ̊",
        " ͂",
        " ̓",
        " ̈́",
        " ͊",
        " ͋",
        " ͌",
        " ̃",
        " ̂",
        " ̌",
        " ͐",
        " ́",
        " ̋",
        " ̏",
        " ̽",
        " ̉",
        " ͣ",
        " ͤ",
        " ͥ",
        " ͦ",
        " ͧ",
        " ͨ",
        " ͩ",
        " ͪ",
        " ͫ",
        " ͬ",
        " ͭ",
        " ͮ",
        " ͯ",
        " ̾",
        " ͛",
        " ͆",
        " ̚",
    ],
    [
        " ̕",
        " ̛",
        " ̀",
        " ́",
        " ͘",
        " ̡",
        " ̢",
        " ̧",
        " ̨",
        " ̴",
        " ̵",
        " ̶",
        " ͜",
        " ͝",
        " ͞",
        " ͟",
        " ͠",
        " ͢",
        " ̸",
        " ̷",
        " ͡",
    ],
]

EMOJIS = [
    "😂",
    "😂",
    "👌",
    "✌",
    "💞",
    "👍",
    "👌",
    "💯",
    "🎶",
    "👀",
    "😂",
    "👓",
    "👏",
    "👐",
    "🍕",
    "💥",
    "🍴",
    "💦",
    "💦",
    "🍑",
    "🍆",
    "😩",
    "😏",
    "👉👌",
    "👀",
    "👅",
    "😩",
    "🚰",
]

INSULT_STRINGS = [
    "Owww ... Such a stupid idiot.",
    "Don't drink and type.",
    "I think you should go home or better a mental asylum.",
    "Command not found. Just like your brain.",
    "Do you realize you are making a fool of yourself? Apparently not.",
    "You can type better than that.",
    "Bot rule 544 section 9 prevents me from replying to stupid humans like you.",
    "Sorry, we do not sell brains.",
    "Believe me you are not normal.",
    "I bet your brain feels as good as new, seeing that you never use it.",
    "If I wanted to kill myself I'd climb your ego and jump to your IQ.",
    "Zombies eat brains... you're safe.",
    "You didn't evolve from apes, they evolved from you.",
    "Come back and talk to me when your I.Q. exceeds your age.",
    "I'm not saying you're stupid, I'm just saying you've got bad luck when it comes to thinking.",
    "What language are you speaking? Cause it sounds like bullshit.",
    "Stupidity is not a crime so you are free to go.",
    "You are proof that evolution CAN go in reverse.",
    "I would ask you how old you are but I know you can't count that high.",
    "As an outsider, what do you think of the human race?",
    "Brains aren't everything. In your case they're nothing.",
    "Ordinarily people live and learn. You just live.",
    "I don't know what makes you so stupid, but it really works.",
    "Keep talking, someday you'll say something intelligent! (I doubt it though)",
    "Shock me, say something intelligent.",
    "Your IQ's lower than your shoe size.",
    "Alas! Your neurotransmitters are no more working.",
    "Are you crazy you fool.",
    "Everyone has the right to be stupid but you are abusing the privilege.",
    "I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.",
    "You should try tasting cyanide.",
    "Your enzymes are meant to digest rat poison.",
    "You should try sleeping forever.",
    "Pick up a gun and shoot yourself.",
    "You could make a world record by jumping from a plane without parachute.",
    "Stop talking BS and jump in front of a running bullet train.",
    "Try bathing with Hydrochloric Acid instead of water.",
    "Try this: if you hold your breath underwater for an hour, you can then hold it forever.",
    "Go Green! Stop inhaling Oxygen.",
    "God was searching for you. You should leave to meet him.",
    "give your 100%. Now, go donate blood.",
    "Try jumping from a hundred story building but you can do it only once.",
    "You should donate your brain seeing that you never used it.",
    "Volunteer for target in an firing range.",
    "Head shots are fun. Get yourself one.",
    "You should try swimming with great white sharks.",
    "You should paint yourself red and run in a bull marathon.",
    "You can stay underwater for the rest of your life without coming back up.",
    "How about you stop breathing for like 1 day? That'll be great.",
    "Try provoking a tiger while you both are in a cage.",
    "Have you tried shooting yourself as high as 100m using a canon.",
    "You should try holding TNT in your mouth and igniting it.",
    "Try playing catch and throw with RDX its fun.",
    "I heard phogine is poisonous but i guess you wont mind inhaling it for fun.",
    "Launch yourself into outer space while forgetting oxygen on Earth.",
    "You should try playing snake and ladders, with real snakes and no ladders.",
    "Dance naked on a couple of HT wires.",
    "Active Volcano is the best swimming pool for you.",
    "You should try hot bath in a volcano.",
    "Try to spend one day in a coffin and it will be yours forever.",
    "Hit Uranium with a slow moving neutron in your presence. It will be a worthwhile experience.",
    "You can be the first person to step on sun. Have a try.",
]

UWUS = [
    "(・`ω´・)",
    ";;w;;",
    "owo",
    "UwU",
    ">w<",
    "^w^",
    r"\(^o\) (/o^)/",
    "( ^ _ ^)∠☆",
    "(ô_ô)",
    "~:o",
    ";-;",
    "(*^*)",
    "(>_",
    "(♥_♥)",
    "*(^O^)*",
    "((+_+))",
]

IWIS = [
    "┐(´д｀)┌",
    "┐(´～｀)┌",
    "┐(´ー｀)┌",
    "┐(￣ヘ￣)┌",
    "╮(╯∀╰)╭",
    "╮(╯_╰)╭",
    "┐(´д`)┌",
    "┐(´∀｀)┌",
    "ʅ(́◡◝)ʃ",
    "┐(ﾟ～ﾟ)┌",
    "┐('д')┌",
    "┐(‘～`;)┌",
    "ヘ(´－｀;)ヘ",
    "┐( -“-)┌",
    "ʅ（´◔౪◔）ʃ",
    "ヽ(゜～゜o)ノ",
    "ヽ(~～~ )ノ",
    "┐(~ー~;)┌",
    "┐(-。ー;)┌",
    r"¯\_(ツ)_/¯",
    r"¯\_(⊙_ʖ⊙)_/¯",
    r"¯\_༼ ಥ ‿ ಥ ༽_/¯",
    "乁( ⁰͡  Ĺ̯ ⁰͡ ) ㄏ",
]

FACEREACTS = [
    "ʘ‿ʘ",
    "ヾ(-_- )ゞ",
    "(っ˘ڡ˘ς)",
    "(´ж｀ς)",
    "( ಠ ʖ̯ ಠ)",
    "(° ͜ʖ͡°)╭∩╮",
    "(ᵟຶ︵ ᵟຶ)",
    "(งツ)ว",
    "ʚ(•｀",
    "(っ▀¯▀)つ",
    "(◠﹏◠)",
    "( ͡ಠ ʖ̯ ͡ಠ)",
    "( ఠ ͟ʖ ఠ)",
    "(∩｀-´)⊃━☆ﾟ.*･｡ﾟ",
    "(⊃｡•́‿•̀｡)⊃",
    "(._.)",
    "{•̃_•̃}",
    "(ᵔᴥᵔ)",
    "♨_♨",
    "⥀.⥀",
    "ح˚௰˚づ ",
    "(҂◡_◡)",
    "ƪ(ړײ)‎ƪ​​",
    "(っ•́｡•́)♪♬",
    "◖ᵔᴥᵔ◗ ♪ ♫ ",
    "(☞ﾟヮﾟ)☞",
    "[¬º-°]¬",
    "(Ծ‸ Ծ)",
    "(•̀ᴗ•́)و ̑̑",
    "ヾ(´〇`)ﾉ♪♪♪",
    "(ง'̀-'́)ง",
    "ლ(•́•́ლ)",
    "ʕ •́؈•̀ ₎",
    "♪♪ ヽ(ˇ∀ˇ )ゞ",
    "щ（ﾟДﾟщ）",
    "( ˇ෴ˇ )",
    "눈_눈",
    "(๑•́ ₃ •̀๑) ",
    "( ˘ ³˘)♥ ",
    "ԅ(≖‿≖ԅ)",
    "♥‿♥",
    "◔_◔",
    "⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾",
    "乁( ◔ ౪◔)「      ┑(￣Д ￣)┍",
    "( ఠൠఠ )ﾉ",
    "٩(๏_๏)۶",
    "┌(ㆆ㉨ㆆ)ʃ",
    "ఠ_ఠ",
    "(づ｡◕‿‿◕｡)づ",
    "(ノಠ ∩ಠ)ノ彡( \\o°o)\\",
    "“ヽ(´▽｀)ノ”",
    "༼ ༎ຶ ෴ ༎ຶ༽",
    "｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡",
    "(づ￣ ³￣)づ",
    "(⊙.☉)7",
    "ᕕ( ᐛ )ᕗ",
    "t(-_-t)",
    "(ಥ⌣ಥ)",
    "ヽ༼ ಠ益ಠ ༽ﾉ",
    "༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽",
    "ミ●﹏☉ミ",
    "(⊙_◎)",
    "¿ⓧ_ⓧﮌ",
    "ಠ_ಠ",
    "(´･_･`)",
    "ᕦ(ò_óˇ)ᕤ",
    "⊙﹏⊙",
    "(╯°□°）╯︵ ┻━┻",
    r"¯\_(⊙︿⊙)_/¯",
    "٩◔̯◔۶",
    "°‿‿°",
    "ᕙ(⇀‸↼‶)ᕗ",
    "⊂(◉‿◉)つ",
    "V•ᴥ•V",
    "q(❂‿❂)p",
    "ಥ_ಥ",
    "ฅ^•ﻌ•^ฅ",
    "ಥ﹏ಥ",
    "（ ^_^）o自自o（^_^ ）",
    "ಠ‿ಠ",
    "ヽ(´▽`)/",
    "ᵒᴥᵒ#",
    "( ͡° ͜ʖ ͡°)",
    "┬─┬﻿ ノ( ゜-゜ノ)",
    "ヽ(´ー｀)ノ",
    "☜(⌒▽⌒)☞",
    "ε=ε=ε=┌(;*´Д`)ﾉ",
    "(╬ ಠ益ಠ)",
    "┬─┬⃰͡ (ᵔᵕᵔ͜ )",
    "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
    r"¯\_(ツ)_/¯",
    "ʕᵔᴥᵔʔ",
    "(`･ω･´)",
    "ʕ•ᴥ•ʔ",
    "ლ(｀ー´ლ)",
    "ʕʘ̅͜ʘ̅ʔ",
    "（　ﾟДﾟ）",
    r"¯\(°_o)/¯",
    "(｡◕‿◕｡)",
]

RUNS_STR = [
    "Runs to Thanos..",
    "Runs far, far away from earth..",
    "Running faster than Bolt coz i'mma userbot !!",
    "Runs to Marie..",
    "This Group is too cancerous to deal with.",
    "Cya bois",
    "Kys",
    "I go away",
    "I am just walking off, coz me is too fat.",
    "I Fugged off!",
    "Will run for chocolate.",
    "I run because I really like food.",
    "Running...\nbecause dieting is not an option.",
    "Wicked fast runnah",
    "If you wanna catch me, you got to be fast...\nIf you wanna stay with me, you got to be good...\nBut if you wanna pass me...\nYou've got to be kidding.",
    "Anyone can run a hundred meters, it's the next forty-two thousand and two hundred that count.",
    "Why are all these people following me?",
    "Are the kids still chasing me?",
    "Running a marathon...there's an app for that.",
]

PRO_STR = [
    "No U ultra pro max extremis supreme super duper hyper premium legendary epic mega omega expert maestro first class adept top-notch excellent magical super-magical superior exceptional dextrous ingenious gawd of gawds pro af teach me how to be pro like you🔥",
    "Pero Gwad Max Plus arrived Noob like me leave",
    "U Pro AF ultra pro max extremis supreme super duper hyper premium legendary epic mega omega expert maestro first class adept top-notch excellent magical super-magical superior exceptional dextrous ingenious gawd of gawds",
    "You you Pro Gwad",
    "You iz Pro Gwad Max Plus, Me iz Noob Gwad Max Plus",
    "You Super Duper Mega Oemega Marvelous Pro Gwad",
    "You you Berry berry Supreme Pro Gwad",
]

CHASE_STR = [
    "Where do you think you're going?",
    "Huh? what? did they get away?",
    "ZZzzZZzz... Huh? what? oh, just them again, nevermind.",
    "Get back here!",
    "Not so fast...",
    "Look out for the wall!",
    "Don't leave me alone with them!!",
    "You run, you die.",
    "Jokes on you, I'm everywhere",
    "You're gonna regret that...",
    "You could also try /kickme, I hear that's fun.",
    "Go bother someone else, no-one here cares.",
    "You can run, but you can't hide.",
    "Is that all you've got?",
    "I'm behind you...",
    "You've got company!",
    "We can do this the easy way, or the hard way.",
    "You just don't get it, do you?",
    "Yeah, you better run!",
    "Please, remind me how much I care?",
    "I'd run faster if I were you.",
    "That's definitely the droid we're looking for.",
    "May the odds be ever in your favour.",
    "Famous last words.",
    "And they disappeared forever, never to be seen again.",
    '"Oh, look at me! I\'m so cool, I can run from a bot!" - this person',
    "Yeah yeah, just tap /kickme already.",
    "Here, take this ring and head to Mordor while you're at it.",
    "Legend has it, they're still running...",
    "Unlike Harry Potter, your parents can't protect you from me.",
    "Fear leads to anger. Anger leads to hate. Hate leads to suffering. If you keep running in fear, you might "
    "be the next Vader.",
    "Multiple calculations later, I have decided my interest in your shenanigans is exactly 0.",
    "Legend has it, they're still running.",
    "Keep it up, not sure we want you here anyway.",
    "You're a wiza- Oh. Wait. You're not Harry, keep moving.",
    "NO RUNNING IN THE HALLWAYS!",
    "Hasta la vista, baby.",
    "Who let the dogs out?",
    "It's funny, because no one cares.",
    "Ah, what a waste. I liked that one.",
    "Frankly, my dear, I don't give a damn.",
    "My milkshake brings all the boys to yard... So run faster!",
    "You can't HANDLE the truth!",
    "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.",
    "Hey, look at them! They're running from the inevitable banhammer... Cute.",
    "Han shot first. So will I.",
    "What are you running after, a white rabbit?",
    "As The Doctor would say... RUN!",
]

HELLOSTR = [
    "Hi !",
    "‘Ello, gov'nor!",
    "What’s crackin’?",
    "‘Sup, homeslice?",
    "Howdy, howdy ,howdy!",
    "Hello, who's there, I'm talking.",
    "You know who this is.",
    "Yo!",
    "Whaddup.",
    "Greetings and salutations!",
    "Hello, sunshine!",
    "Hey, howdy, hi!",
    "What’s kickin’, little chicken?",
    "Peek-a-boo!",
    "Howdy-doody!",
    "Hey there, freshman!",
    "I come in peace!",
    "Ahoy, matey!",
    "Hiya!",
]

SHGS = [
    "┐(´д｀)┌",
    "┐(´～｀)┌",
    "┐(´ー｀)┌",
    "┐(￣ヘ￣)┌",
    "╮(╯∀╰)╭",
    "╮(╯_╰)╭",
    "┐(´д`)┌",
    "┐(´∀｀)┌",
    "ʅ(́◡◝)ʃ",
    "┐(ﾟ～ﾟ)┌",
    "┐('д')┌",
    "┐(‘～`;)┌",
    "ヘ(´－｀;)ヘ",
    "┐( -“-)┌",
    "ʅ（´◔౪◔）ʃ",
    "ヽ(゜～゜o)ノ",
    "ヽ(~～~ )ノ",
    "┐(~ー~;)┌",
    "┐(-。ー;)┌",
    r"¯\_(ツ)_/¯",
    r"¯\_(⊙_ʖ⊙)_/¯",
    r"¯\_༼ ಥ ‿ ಥ ༽_/¯",
    "乁( ⁰͡  Ĺ̯ ⁰͡ ) ㄏ",
]

CRI = [
    "أ‿أ",
    "╥﹏╥",
    "(;﹏;)",
    "(ToT)",
    "(┳Д┳)",
    "(ಥ﹏ಥ)",
    "（；へ：）",
    "(T＿T)",
    "（πーπ）",
    "(Ｔ▽Ｔ)",
    "(⋟﹏⋞)",
    "（ｉДｉ）",
    "(´Д⊂ヽ",
    "(;Д;)",
    "（>﹏<）",
    "(TдT)",
    "(つ﹏⊂)",
    "༼☯﹏☯༽",
    "(ノ﹏ヽ)",
    "(ノAヽ)",
    "(╥_╥)",
    "(T⌓T)",
    "(༎ຶ⌑༎ຶ)",
    "(☍﹏⁰)｡",
    "(ಥ_ʖಥ)",
    "(つд⊂)",
    "(≖͞_≖̥)",
    "(இ﹏இ`｡)",
    "༼ಢ_ಢ༽",
    "༼ ༎ຶ ෴ ༎ຶ༽",
]

SLAP_TEMPLATES = [
    "{hits} {victim} with a {item}.",
    "{hits} {victim} in the face with a {item}.",
    "{hits} {victim} around a bit with a {item}.",
    "{throws} a {item} at {victim}.",
    "grabs a {item} and {throws} it at {victim}'s face.",
    "{hits} a {item} at {victim}.",
    "{throws} a few {item} at {victim}.",
    "grabs a {item} and {throws} it in {victim}'s face.",
    "launches a {item} in {victim}'s general direction.",
    "sits on {victim}'s face while slamming a {item} {where}.",
    "starts slapping {victim} silly with a {item}.",
    "pins {victim} down and repeatedly {hits} them with a {item}.",
    "grabs up a {item} and {hits} {victim} with it.",
    "starts slapping {victim} silly with a {item}.",
    "holds {victim} down and repeatedly {hits} them with a {item}.",
    "prods {victim} with a {item}.",
    "picks up a {item} and {hits} {victim} with it.",
    "ties {victim} to a chair and {throws} a {item} at them.",
    "{hits} {victim} {where} with a {item}.",
    "ties {victim} to a pole and whips them {where} with a {item}."
    "gave a friendly push to help {victim} learn to swim in lava.",
    "sent {victim} to /dev/null.",
    "sent {victim} down the memory hole.",
    "beheaded {victim}.",
    "threw {victim} off a building.",
    "replaced all of {victim}'s music with Nickelback.",
    "spammed {victim}'s email.",
    "made {victim} a knuckle sandwich.",
    "slapped {victim} with pure nothing.",
    "hit {victim} with a small, interstellar spaceship.",
    "quickscoped {victim}.",
    "put {victim} in check-mate.",
    "RSA-encrypted {victim} and deleted the private key.",
    "put {victim} in the friendzone.",
    "slaps {victim} with a DMCA takedown request!",
]

ITEMS = [
    "cast iron skillet",
    "large trout",
    "baseball bat",
    "cricket bat",
    "wooden cane",
    "nail",
    "printer",
    "shovel",
    "pair of trousers",
    "CRT monitor",
    "diamond sword",
    "baguette",
    "physics textbook",
    "toaster",
    "portrait of Richard Stallman",
    "television",
    "mau5head",
    "five ton truck",
    "roll of duct tape",
    "book",
    "laptop",
    "old television",
    "sack of rocks",
    "rainbow trout",
    "cobblestone block",
    "lava bucket",
    "rubber chicken",
    "spiked bat",
    "gold block",
    "fire extinguisher",
    "heavy rock",
    "chunk of dirt",
    "beehive",
    "piece of rotten meat",
    "bear",
    "ton of bricks",
]

THROW = [
    "throws",
    "flings",
    "chucks",
    "hurls",
]

HIT = [
    "hits",
    "whacks",
    "slaps",
    "smacks",
    "bashes",
]


WHERE = ["in the chest", "on the head", "on the butt", "on the crotch"]


GM_STR = [
    "Wishing you a day full of sunny smiles and happy thoughts\n\n~~Good Morning!",
    "Every Morning we are born again, what we do today is what matters the most\n\n~~Good Morning!",
    "A new day\nA new Blessing\nA new hope\n\n~~Good Morning!",
    "Sometimes the best thing you can do is \nNot think, Not stress\nNot wonder, Not obsess\nJust breathe and have faith,\nEverything will work out...\nJust Live\n\n~~Good Morning!",
    "Get up everyday with a positive mission...\n Because you deserve to live an Amazing life! \n\n~~Good Morning!",
    "Never think\n I have nothing... \n\n Never think\n I have everything...\n\n But always think\n I have something\n and I can achieve everything!\n\n~~Good Morning!",
    "Road has speed limit,\nbank has money limit,\nExams have time limit,\n BUT\nYour thinking has no limit,\nSo think big, \n and Achieve Big,\n\n~~Good Morning!",
    "God didn't create us to be sad,\nHe created us to have joy\n\n~~Good Morning!",
    "You are a rare gem,an exclusive, a limitd edition.\n There is only one of you! Have an amazing day!\n\n~~Good Morning!",
    "Stay Hopeful\nYou never know\nWhat this day can bring.\n\n~~Good Morning!",
    "Between\nYesterday's mistake &\nTomorrow's Hope,\nthere is a \nfantastic opportunity called\n**Today**,\nLive it! Love it!\nThis day is yours!\n\n~~Good Morning!",
    "Living is very simple,\nLoving is also simple\nLaughing is too simple,\nWinning is also simple,\nThen what is difficult?\nBeing simple is very difficult\n\nGood Morning!"
]


    
# ===========================================


@register(outgoing=True, pattern=r"^.(\w+)say (.*)")
async def univsaye(cowmsg):
    """ For .cowsay module, userbot wrapper for cow which says things. """
    arg = cowmsg.pattern_match.group(1).lower()
    text = cowmsg.pattern_match.group(2)

    if arg == "cow":
        arg = "default"
    if arg not in cow.COWACTERS:
        return
    cheese = cow.get_cow(arg)
    cheese = cheese()

    await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")


@register(outgoing=True, pattern="^:/$", ignore_unsafe=True)
async def kek(keks):
    """ Check yourself ;)"""
    uio = ["/", "\\"]
    for i in range(1, 15):
        time.sleep(0.3)
        await keks.edit(":" + uio[i % 2])


@register(outgoing=True, pattern=r"^.coinflip (.*)")
async def coin(event):
    r = choice(["heads", "tails"])
    input_str = event.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r == "heads":
        if input_str == "heads":
            await event.edit("The coin landed on: **Heads**.\nYou were correct.")
        elif input_str == "tails":
            await event.edit(
                "The coin landed on: **Heads**.\nYou weren't correct, try again ..."
            )
        else:
            await event.edit("The coin landed on: **Heads**.")
    elif r == "tails":
        if input_str == "tails":
            await event.edit("The coin landed on: **Tails**.\nYou were correct.")
        elif input_str == "heads":
            await event.edit(
                "The coin landed on: **Tails**.\nYou weren't correct, try again ..."
            )
        else:
            await event.edit("The coin landed on: **Tails**.")


@register(pattern="^.slap(?: |$)(.*)", outgoing=True)
async def who(event):
    """ slaps a user, or get slapped if not a reply. """
    replied_user = await get_user_from_event(event)
    if replied_user:
        replied_user = replied_user[0]
    else:
        return
    caption = await slap(replied_user, event)

    try:
        await event.edit(caption)

    except BaseException:
        await event.edit(
            "`Can't slap this person, need to fetch some sticks and stones !!`"
        )


async def slap(replied_user, event):
    """ Construct a funny slap sentence !! """
    user_id = replied_user.id
    first_name = replied_user.first_name
    username = replied_user.username

    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = choice(SLAP_TEMPLATES)
    item = choice(ITEMS)
    hit = choice(HIT)
    throw = choice(THROW)
    where = choice(WHERE)

    caption = "..." + temp.format(
        victim=slapped, item=item, hits=hit, throws=throw, where=where
    )

    return caption


@register(outgoing=True, pattern="^-_-$", ignore_unsafe=True)
async def emo(sigh):
    """Ok..."""
    okay = "-_-"
    for i in range(10):
        okay = okay[:-1] + "_-"
        await sigh.edit(okay)


@register(outgoing=True, pattern="^.(yes|no|maybe|decide)$")
async def decide(event):
    decision = event.pattern_match.group(1).lower()
    message_id = event.reply_to_msg_id if event.reply_to_msg_id else None
    if decision != "decide":
        r = requests.get(f"https://yesno.wtf/api?force={decision}").json()
    else:
        r = requests.get(f"https://yesno.wtf/api").json()
    await event.delete()
    await event.client.send_message(
        event.chat_id, str(r["answer"]).upper(), reply_to=message_id, file=r["image"]
    )


@register(outgoing=True, pattern="^;_;$", ignore_unsafe=True)
async def fun(idk):
    t = ";_;"
    for j in range(10):
        t = t[:-1] + "_;"
        await idk.edit(t)


@register(outgoing=True, pattern="^.fp$")
async def facepalm(palm):
    """Facepalm  🤦‍♂"""
    await palm.edit("🤦‍♂")


@register(outgoing=True, pattern="^.cry$")
async def cry(cying):
    """y u du dis, i cry everytime !!"""
    await cying.edit(choice(CRI))


@register(outgoing=True, pattern="^.insult$")
async def insult(rude):
    """I make you cry !!"""
    await rude.edit(choice(INSULT_STRINGS))


@register(outgoing=True, pattern="^.killer$(.*)")
async def killer(koller):
    await koller.edit(
        f"__**Commando **__{DEF}          \n\n"
        "_/﹋\_\n"
        "(҂`_´)\n"
        f"<,︻╦╤─ ҉ - - - {name}\n"
        "_/﹋\_\n",
    )
                      
@register(outgoing=True, pattern="^.bruh$")
async def bruh(tard):
    bruhdir = "resources/bruh.mp3"
    message_id = tard.reply_to_msg_id if tard.reply_to_msg_id else None
    await tard.delete()
    await tard.client.send_file(
        tard.chat_id, 
        bruhdir,
        reply_to=message_id
    )
                      
@register(outgoing=True, pattern="^.pero$")
async def pero(pru):
    pro = "resources/pro.ogg"
    message.id = pru.reply.message.id if pru.repy_to_msd_id else None
    await pru.delete()
    await pru.client.send_file(
        pru.chat,id,
        pro,
        reply_to=message_id
    )
                      
                      
@register(outgoing=True, pattern="^.cp(?: |$)(.*)")
async def copypasta(cp_e):
    """ Copypasta the famous meme """
    textx = await cp_e.get_reply_message()
    message = cp_e.pattern_match.group(1)

    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await cp_e.edit("`😂🅱️IvE👐sOME👅text👅for✌️Me👌tO👐MAkE👀iT💞funNy!💦`")
        return

    reply_text = choice(EMOJIS)
    # choose a random character in the message to be substituted with 🅱️
    b_char = choice(message).lower()
    for owo in message:
        if owo == " ":
            reply_text += choice(EMOJIS)
        elif owo in EMOJIS:
            reply_text += owo
            reply_text += choice(EMOJIS)
        elif owo.lower() == b_char:
            reply_text += "🅱️"
        else:
            if bool(getrandbits(1)):
                reply_text += owo.upper()
            else:
                reply_text += owo.lower()
    reply_text += choice(EMOJIS)
    await cp_e.edit(reply_text)


@register(outgoing=True, pattern="^.vapor(?: |$)(.*)")
async def vapor(vpr):
    """ Vaporize everything! """
    reply_text = list()
    textx = await vpr.get_reply_message()
    message = vpr.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await vpr.edit("`Ｇｉｖｅ ｓｏｍｅ ｔｅｘｔ ｆｏｒ ｖａｐｏｒ！`")
        return

    for charac in message:
        if 0x21 <= ord(charac) <= 0x7F:
            reply_text.append(chr(ord(charac) + 0xFEE0))
        elif ord(charac) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(charac)

    await vpr.edit("".join(reply_text))


@register(outgoing=True, pattern="^.str(?: |$)(.*)")
async def stretch(stret):
    """ Stretch it."""
    textx = await stret.get_reply_message()
    message = stret.text
    message = stret.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await stret.edit("`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")
        return

    count = randint(3, 10)
    reply_text = sub(r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])", (r"\1" * count), message)
    await stret.edit(reply_text)


@register(outgoing=True, pattern="^.zal(?: |$)(.*)")
async def zal(zgfy):
    """ Invoke the feeling of chaos. """
    reply_text = list()
    textx = await zgfy.get_reply_message()
    message = zgfy.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await zgfy.edit(
            "`gͫ ̆ i̛ ̺ v͇̆ ȅͅ   a̢ͦ   s̴̪ c̸̢ ä̸ rͩͣ y͖͞   t̨͚ é̠ x̢͖  t͔͛`"
        )
        return

    for charac in message:
        if not charac.isalpha():
            reply_text.append(charac)
            continue

        for _ in range(0, 3):
            textz = randint(0, 2)

            if textz == 0:
                charac = charac.strip() + choice(ZALG_LIST[0]).strip()
            elif textz == 1:
                charac = charac.strip() + choice(ZALG_LIST[1]).strip()
            else:
                charac = charac.strip() + choice(ZALG_LIST[2]).strip()

        reply_text.append(charac)

    await zgfy.edit("".join(reply_text))


@register(outgoing=True, pattern="^.hi$")
async def hoi(hello):
    """ Greet everyone! """
    await hello.edit(choice(HELLOSTR))


@register(outgoing=True, pattern="^.owo(?: |$)(.*)")
async def face(owo):
    """UwU"""
    textx = await owo.get_reply_message()
    message = owo.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await owo.edit("` UwU no text given! `")
        return

    reply_text = sub(r"(r|l)", "w", message)
    reply_text = sub(r"(R|L)", "W", reply_text)
    reply_text = sub(r"n([aeiou])", r"ny\1", reply_text)
    reply_text = sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
    reply_text = sub(r"\!+", " " + choice(UWUS), reply_text)
    reply_text = reply_text.replace("ove", "uv")
    reply_text += " " + choice(UWUS)
    await owo.edit(reply_text)


@register(outgoing=True, pattern="^.react$")
async def react_meme(react):
    """ Make your userbot react to everything. """
    await react.edit(choice(FACEREACTS))


@register(outgoing=True, pattern="^.iwi(?: |$)(.*)")
async def faces(siwis):
    """ IwI """
    textx = await siwis.get_reply_message()
    message = siwis.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await siwis.edit("` IwI no text given! `")
        return

    reply_text = sub(r"(a|i|u|e|o)", "i", message)
    reply_text = sub(r"(A|I|U|E|O)", "I", reply_text)
    reply_text = sub(r"\!+", " " + choice(IWIS), reply_text)
    reply_text += " " + choice(IWIS)
    await siwis.edit(reply_text)


@register(outgoing=True, pattern="^.shg$")
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    await shg.edit(choice(SHGS))


@register(outgoing=True, pattern="^.chase$")
async def police(chase):
    """ Run boi run, i'm gonna catch you !! """
    await chase.edit(choice(CHASE_STR))


@register(outgoing=True, pattern="^.run$")
async def runner_lol(run):
    """ Run, run, RUNNN! """
    await run.edit(choice(RUNS_STR))
                     
                      
@register(outgoing=True, pattern="^.pro$")
async def pro(peru):
    """ Right Back To Pros """                 
    await peru.edit(choice(PRO_STR))
                      
@register(outgoing=True, pattern="^.m$")
async def m(morni):
    """ Good Morning Greetings """
    await morni.edit(choice(GM_STR))
                      
@register(outgoing=True, pattern="^.metoo$")
async def metoo(hahayes):
    """ Haha yes """
    await hahayes.edit(choice(METOOSTR))


@register(outgoing=True, pattern="^.iff$")
async def pressf(f):
    """Pays respects"""
    args = f.text.split()
    arg = (f.text.split(" ", 1))[1] if len(args) > 1 else None
    if len(args) == 1:
        r = randint(0, 3)
        LOGS.info(r)
        if r == 0:
            await f.edit("┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
        elif r == 1:
            await f.edit("╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯")
        else:
            arg = "F"
    if arg is not None:
        out = ""
        F_LENGTHS = [5, 1, 1, 4, 1, 1, 1]
        for line in F_LENGTHS:
            c = max(round(line / len(arg)), 1)
            out += (arg * c) + "\n"
        await f.edit("`" + out + "`")


@register(outgoing=True, pattern="^oof$")
async def oof(woof):
    t = "oof"
    for j in range(25):
        t = t[:-1] + "of"
        await woof.edit(t)


@register(outgoing=True, pattern="^yeee$")
async def yeee(yeah):
    t = "yeee"
    for j in range(25):
        t = t[:-1] + "ee"
        await yeah.edit(t)


@register(outgoing=True, pattern="^Proo$")
async def Pro(proo):
    t = "Proo"
    for j in range(20):
        t = t[:-1] + "oo"
        await proo.edit(t)                      
                     

@register(outgoing=True, pattern="^Brr$")
async def Brr(burr):
    t = "Brr"
    for j in range(20):
        t = t[:-1] + "rr"
        await burr.edit(t)

@register(outgoing=True, pattern="^Prr$")
async def Prr(burr):
    t = "Prr"
    for j in range(20):
        t = t[:-1] + "rr"
        await burr.edit(t)

@register(outgoing=True, pattern="^hmm$")
async def hmm(hmmm):
    t = "hmm"
    for j in range(10):
        t = t[:-1] + "mm"
        await hmmm.edit(t)
                      
                      
@register(outgoing=True, pattern="^Noo$")
async def Noo(nooo):
    t = "Noo"
    for j in range(25):
        t = t[:-1] + "oo"
        await nooo.edit(t)
                      
@register(outgoing=True, pattern="^Eww$")
async def Eww(Ewe):
    t = "Eww"
    for j in range(20):
        t = t[:-1] + "ww"
        await Ewe.edit(t)                      
                      
@register(outgoing=True, pattern="^.moon$")
async def moon(moone):
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    try:
        for x in range(32):
            await sleep(0.1)
            await moone.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.earth$")
async def earth(event):
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.boxes$")
async def boxes(event):
    deq = deque(list("🟥🟧🟨🟩🟦🟪🟫⬛⬜"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return                     


@register(outgoing=True, pattern="^.hmm$")
async def hmm(event):
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.haha$")
async def haha(event):
    deq = deque(list("😂🤣😂🤣😂🤣"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.rain$")
async def rain(event):
    deq = deque(list("🌬☁️🌩🌨🌧🌦🌥⛅🌤"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.clock$")
async def clock(event):
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return

@register(outgoing=True, pattern="^.operations$")
async def operations(event):
    deq = deque(list("!@#$%^&*()_+="))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return

                      
@register(outgoing=True, pattern="^.mock(?: |$)(.*)")
async def spongemocktext(mock):
    """ Do it and find the real fun. """
    reply_text = list()
    textx = await mock.get_reply_message()
    message = mock.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await mock.edit("`gIvE sOMEtHInG tO MoCk!`")
        return

    for charac in message:
        if charac.isalpha() and randint(0, 1):
            to_app = charac.upper() if charac.islower() else charac.lower()
            reply_text.append(to_app)
        else:
            reply_text.append(charac)

    await mock.edit("".join(reply_text))


@register(outgoing=True, pattern="^.clap(?: |$)(.*)")
async def claptext(memereview):
    """ Praise people! """
    textx = await memereview.get_reply_message()
    message = memereview.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await memereview.edit("`Hah, I don't clap pointlessly!`")
        return
    reply_text = "👏 "
    reply_text += message.replace(" ", " 👏 ")
    reply_text += " 👏"
    await memereview.edit(reply_text)


@register(outgoing=True, pattern="^.bt$")
async def bluetext(bt_e):
    """ Believe me, you will find this useful. """
    if await bt_e.get_reply_message() and bt_e.is_group:
        await bt_e.edit(
            "/BLUETEXT /MUST /CLICK.\n"
            "/ARE /YOU /A /STUPID /ANIMAL /WHICH /IS /ATTRACTED /TO /COLOURS?"
        )


@register(outgoing=True, pattern=r"^.f (.*)")
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8,
        paytext * 8,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 6,
        paytext * 6,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
    )
    await event.edit(pay)


@register(outgoing=True, pattern="^.lfy (.*)")
async def let_me_google_that_for_you(lmgtfy_q):
    textx = await lmgtfy_q.get_reply_message()
    qry = lmgtfy_q.pattern_match.group(1)
    if qry:
        query = str(qry)
    elif textx:
        query = textx
        query = query.message
    query_encoded = query.replace(" ", "+")
    lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
    payload = {"format": "json", "url": lfy_url}
    r = requests.get("http://is.gd/create.php", params=payload)
    await lmgtfy_q.edit(
        f"Here you are, help yourself.\
    \n[{query}]({r.json()['shorturl']})"
    )


@register(pattern=r".scam(?: |$)(.*)", outgoing=True)
async def scam(event):
    """ Just a small command to fake chat actions for fun !! """
    options = [
        "typing",
        "contact",
        "game",
        "location",
        "voice",
        "round",
        "video",
        "photo",
        "document",
        "cancel",
    ]
    input_str = event.pattern_match.group(1)
    args = input_str.split()
    if len(args) == 0:  # Let bot decide action and time
        scam_action = choice(options)
        scam_time = randint(30, 60)
    elif len(args) == 1:  # User decides time/action, bot decides the other.
        try:
            scam_action = str(args[0]).lower()
            scam_time = randint(30, 60)
        except ValueError:
            scam_action = choice(options)
            scam_time = int(args[0])
    elif len(args) == 2:  # User decides both action and time
        scam_action = str(args[0]).lower()
        scam_time = int(args[1])
    else:
        await event.edit("`Invalid Syntax !!`")
        return
    try:
        if scam_time > 0:
            await event.delete()
            async with event.client.action(event.chat_id, scam_action):
                await sleep(scam_time)
    except BaseException:
        return


@register(pattern=r".type(?: |$)(.*)", outgoing=True)
async def typewriter(typew):
    """ Just a small command to make your keyboard become a typewriter! """
    textx = await typew.get_reply_message()
    message = typew.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await typew.edit("`Give a text to type!`")
        return
    sleep_time = 0.03
    typing_symbol = "|"
    old_text = ""
    await typew.edit(typing_symbol)
    await sleep(sleep_time)
    for character in message:
        old_text = old_text + "" + character
        typing_text = old_text + "" + typing_symbol
        await typew.edit(typing_text)
        await sleep(sleep_time)
        await typew.edit(old_text)
        await sleep(sleep_time)


@register(outgoing=True, pattern="^.fail$")
async def fail(faill):
    if not faill.text[0].isalpha() and faill.text[0] not in ("/", "#", "@", "!"):
        await faill.edit(
            "`\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ `"
            "`\n████▌▄▌▄▐▐▌█████ `"
            "`\n████▌▄▌▄▐▐▌▀████ `"
            "`\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ `"
        )


@register(outgoing=True, pattern="^.lol$")
async def lol(lel):
    if not lel.text[0].isalpha() and lel.text[0] not in ("/", "#", "@", "!"):
        await lel.edit(
            "`\n╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ `"
            "`\n╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ `"
            "`\n╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ `"
            "`\n╱┗━━━┛╰━━━╯┗━━━┛╱ `"
        )
       
@register(outgoing=True, pattern="^.lmao$")
async def lmao(lmfao):
    if not lmfao.text[0].isalpha() and lmfao.text[0] not in ("/", "#", "@", "!"):
        await lmfao.edit(
            "`\n░█─── ░█▀▄▀█ ─█▀▀█ ░█▀▀▀█`"
            "`\n░█─── ░█░█░█ ░█▄▄█ ░█──░█`"
            "`\n░█▄▄█ ░█──░█ ░█─░█ ░█▄▄▄█`"
        )
        
@register(outgoing=True, pattern="^.pig$")
async def pig(poog):
    if not poog.text[0].isalpha() and poog.text[0] not in ("/", "#", "@", "!"):
        await poog.edit(
                "\n┈┈┏━╮╭━┓┈╭━━━━╮"
                "\n┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃"
                "\n┈┈╰┓▋▋┏╯╯╰━━━━╯"
                "\n┈╭━┻╮╲┗━━━━╮╭╮┈"
                "\n┈┃▎▎┃╲╲╲╲╲╲┣━╯┈"
                "\n┈╰━┳┻▅╯╲╲╲╲┃┈┈┈"
                "\n┈┈┈╰━┳┓┏┳┓┏╯┈┈┈"
                "\n┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈"
        )


@register(outgoing=True, pattern="^.gun$")
async def gun(gan):
    if not gan.text[0].isalpha() and gan.text[0] not in ("/", "#", "@", "!"):
        await gan.edit(
                "\n░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄"
                "\n░███████████████████████ "
                "\n░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤ "
                "\n░▀░▐▓▓▓▓▓▓▌▀█░░░█▀░"
                "\n░░░▓▓▓▓▓▓█▄▄▄▄▄█▀░░"
                "\n░░█▓▓▓▓▓▌░░░░░░░░░░"
                "\n░▐█▓▓▓▓▓░░░░░░░░░░░"
                "\n░▐██████▌░░░░░░░░░░"
        )

@register(outgoing=True, pattern="^.troll$")
async def troll(troll):
    if not troll.text[0].isalpha() and troll.text[0] not in ("/", "#", "@", "!"):
        await troll.edit(
                      " ⠛⢻⣿⣯⣿⣿⣿⣶ ⣶⣶⣶⣤⣤⣤⣀\n"
                      "      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷\n"
                      "           ⠻⣿⡛⠉⠭⠉⠉⢉⣿⣿⣧\n"
                      "  ⠈⠙⠲⣶⠖⠄⠄⢿⣿⠄⠶⣶⣾⣿⣿⣿⣿⣧\n"                    
                      "           ⠺⢿⡗⠄⣹⣿⣿⠿⣟⣿⡏\n"  
                      "             ⠤⠤⢾⣿⣿⣿⣦⠘⡿\n"
                      "        ⠈⢻⡿⣷⣶⣶⣤⣤⣤⣶⣦⠁\n"
                      "       ⠄⣽⣿⣿⣿⣿⣿⣿⣿⣿⡟⠘\n"
                      "         ⠿⣿⣿⣿⣿⣿⣿⣿⠃\n"
                      "            ⠉⠉⠛⠋⠉⠁\n"
                     )
            
@register(outgoing=True, pattern="^.lool$")
async def lool(lul):
    if not lul.text[0].isalpha() and lul.text[0] not in ("/", "#", "@", "!"):
        await lul.edit(
            "`\n╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈\n┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈\n┈┃┃╱▔▔▔▔▔▔▔▏╱▋▋╮┈`"
            "`\n┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃┈\n┈╰━▏┗━╰╯┗━╱╱╱╰┻┫┈\n┈┈┈▏┏┳━━━━▏┏┳━━╯┈`"
            "`\n┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈ `"
        )
        
@register(outgoing=True, pattern="^.snake$")
async def snake(snuk):
    if not snuk.text[0].isalpha() and snuk.text[0] not in ("/", "#", "@", "!"):
        await snuk.edit(
            "░░░░▓\n"
            "░░░▓▓\n"
            "░░█▓▓█\n"
            "░██▓▓██\n"
            "░░██▓▓██\n"
            "░░░██▓▓██\n"
            "░░░░██▓▓██\n"
            "░░░░░██▓▓██\n"
            "░░░░██▓▓██\n"
            "░░░██▓▓██\n"
            "░░██▓▓██\n"
            "░██▓▓██\n"
            "░░██▓▓██\n"
            "░░░██▓▓██\n"
            "░░░░██▓▓██\n"
            "░░░░░██▓▓██\n"
            "░░░░██▓▓██\n"
            "░░░██▓▓██\n"
            "░░██▓▓██\n"
            "░██▓▓██\n"
            "░░██▓▓██\n"
            "░░░██▓▓██\n"
            "░░░░██▓▓██\n"
            "░░░░░██▓▓██\n"
            "░░░░██▓▓██\n"
            "░░░██▓▓██\n"
            "░░██▓▓██\n"
            "░██▓▓██\n"
            "░░██▓▓██\n"
            "░░░██▓▓██\n"
            "░░░░██▓▓██\n"
            "░░░░░██▓▓██\n"
            "░░░░██▓▓██\n"
            "░░░██▓▓██\n"
            "░░██▓▓██\n"
            "░██▓▓██\n"
            "░░██▓▓██\n"
            "░░░██▓▓██\n"
            "░░░░██▓▓██\n"
            "░░░░░██▓▓██\n"
            "░░░░██▓▓██\n"
            "░░░██▓▓██\n"
            "░░██▓▓██\n"
            "░██▓▓██\n"
            "░░██▓▓██\n"
            "░░░██▓▓██\n"
            "░░░░██▓▓██\n"
            "░░░░░██▓▓██\n"
            "░░░░██▓▓██\n"
            "░░░██▓▓██\n"
            "░░██▓▓██\n"
            "░██▓▓██\n"
            "░░██▓▓██\n"
            "░░░██▓▓██\n"
            "░░░░██▓▓██\n"
            "░░░░░██▓▓██\n"
            "░░░░██▓▓██\n"
            "░░░██▓▓██\n"
            "░░██▓▓██\n"
            "░██▓▓██\n"
            "░░██▓▓██\n"
            "░░░██▓▓██\n"
            "░░░░██▓▓██\n"
            "░░░░░██▓▓██\n"
            "░░░░██▓▓██\n"
            "░░░██▓▓██\n"
            "░░██▓▓██\n"
            "░░██▓▓██\n"
            "░░██▓▓██\n"
            "░░██▓▓██\n"
            "░░██▓▓██\n"
            "░░██▓▓██\n"
            "░░░██▓▓███\n"
            "░░░░██▓▓████\n"
            "░░░░░██▓▓█████\n"
            "░░░░░░██▓▓██████\n"
            "░░░░░░███▓▓███████\n"
            "░░░░░████▓▓████████\n"
            "░░░░█████▓▓█████████\n"
            "░░░█████░░░█████●███\n"
            "░░████░░░░░░░███████\n"
            "░░███░░░░░░░░░██████\n"
            "░░██░░░░░░░░░░░████\n"
            "░░░░░░░░░░░░░░░░███\n"
            "░░░░░░░░░░░░░░░░░░░\n"
        )


@register(outgoing=True, pattern="^.india$")
async def india(ind):
    if not ind.text[0].isalpha() and ind.text[0] not in ("/", "#", "@", "!"):
        await ind.edit(
        "⣿⣿⣿⣿⣿⣍⠀⠉⠻⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⠓⠀⠀⢒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿\n"
        "⣿⡿⠋⠋⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⢿⣿⣿⡿⣿⣿⡟⠋⠀⢀⣩\n"
        "⣿⣿⡄⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀⠀⠈⠉⠛⢷⣭⠉⠁⠀⠀⣿⣿\n"
        "⣇⣀. INDIA🇮🇳INDIA🇮🇳⠆⠠..⠘⢷⣿⣿⣛⠐⣶⣿⣿\n"
        "⣿⣄⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⣠⣿⣿⣿⣾⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⠀⠀⠂⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        )


@register(outgoing=True, pattern="^.stfu$")
async def stfu(shutup):
    if not shutup.text[0].isalpha() and shutup.text[0] not in ("/", "#", "@", "!"):
        await shutup.edit(
            "`\n█████████████████████████████████`"
            "`\n██▀▀▀▀████▀▀▀▀████▀▀▀▀▀███▀▀██▀▀█`"
            "`\n█──────██──────██───────██──██──█`"
            "`\n█──██▄▄████──████──███▄▄██──██──█`"
            "`\n█▄────▀████──████────█████──██──█`"
            "`\n█▀▀██──████──████──███████──██──█`"
            "`\n█──────████──████──███████──────█`"
            "`\n██▄▄▄▄█████▄▄████▄▄████████▄▄▄▄██`"
            "`\n█████████████████████████████████`"
        )


@register(outgoing=True, pattern="^.gtfo$")
async def gtfo(getout):
    if not getout.text[0].isalpha() and getout.text[0] not in ("/", "#", "@", "!"):
        await getout.edit(
            "`\n███████████████████████████████ `"
            "`\n█▀▀▀▀▀▀▀█▀▀▀▀▀▀█▀▀▀▀▀▀▀█▀▀▀▀▀▀█ `"
            "`\n█───────█──────█───────█──────█ `"
            "`\n█──███──███──███──███▄▄█──██──█ `"
            "`\n█──███▄▄███──███─────███──██──█ `"
            "`\n█──██───███──███──██████──██──█ `"
            "`\n█──▀▀▀──███──███──██████──────█ `"
            "`\n█▄▄▄▄▄▄▄███▄▄███▄▄██████▄▄▄▄▄▄█ `"
            "`\n███████████████████████████████ `"
        )


@register(outgoing=True, pattern="^.nih$")
async def nih(rose):
    if not rose.text[0].isalpha() and rose.text[0] not in ("/", "#", "@", "!"):
        await rose.edit(
            r"`(\_/)`"
            "`\n(●_●)`"
            "`\n />🌹 *ini buat kamu`"
            "\n\n"
            r"`(\_/)`"
            "`\n(●_●)\n`"
            r"`🌹<\  *tapi boong`"
        )


@register(outgoing=True, pattern="^.fag$")
async def ugay(faggot):
    if not faggot.text[0].isalpha() and faggot.text[0] not in ("/", "#", "@", "!"):
        await faggot.edit(
            "`\n█████████`"
            "`\n█▄█████▄█`"
            "`\n█▼▼▼▼▼`"
            "`\n█       STFU FAGGOT'S`"
            "`\n█▲▲▲▲▲`"
            "`\n█████████`"
            "`\n ██   ██`"
        )


@register(outgoing=True, pattern="^.taco$")
async def taco(tacoo):
    if not tacoo.text[0].isalpha() and tacoo.text[0] not in ("/", "#", "@", "!"):
        await tacoo.edit(r"\n{\__/}" "\n(●_●)" "\n( >🌮 Want a taco?")


@register(outgoing=True, pattern="^.paw$")
async def paw(pawed):
    if not pawed.text[0].isalpha() and pawed.text[0] not in ("/", "#", "@", "!"):
        await pawed.edit("`(=ↀωↀ=)")


@register(outgoing=True, pattern="^.tf$")
async def tf(focc):
    if not focc.text[0].isalpha() and focc.text[0] not in ("/", "#", "@", "!"):
        await focc.edit("(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄  ")


@register(outgoing=True, pattern="^.gey$")
async def gey(gai):
    if not gai.text[0].isalpha() and gai.text[0] not in ("/", "#", "@", "!"):
        await gai.edit(
            "`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
            "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
            "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈NIGGA U GEY`"
            "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈"
        )


@register(outgoing=True, pattern="^.gay$")
async def gay(ugay):
    if not ugay.text[0].isalpha() and ugay.text[0] not in ("/", "#", "@", "!"):
        await ugay.edit(
            "`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
            "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
            "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈BAPAQ U GAY`"
            "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈"
        )


@register(outgoing=True, pattern="^.bot$")
async def bot(robot):
    if not robot.text[0].isalpha() and robot.text[0] not in ("/", "#", "@", "!"):
        await robot.edit(
            "` \n   ╲╲╭━━━━╮ \n╭╮┃▆┈┈▆┃╭╮ \n┃╰┫▽▽▽┣╯┃ \n╰━┫△△△┣━╯`"
            "`\n╲╲┃┈┈┈┈┃  \n╲╲┃┈┏┓┈┃ `"
        )


@register(outgoing=True, pattern="^.hey$")
async def hey(heyo):
    if not heyo.text[0].isalpha() and heyo.text[0] not in ("/", "#", "@", "!"):
        await heyo.edit(
            "\n┈┈┈╱▔▔▔▔╲┈╭━━━━━\n┈┈▕▂▂▂▂▂▂▏┃HEY!┊😀`"
            "`\n┈┈▕▔▇▔▔┳▔▏╰┳╮HEY!┊\n┈┈▕╭━╰╯━╮▏━╯╰━━━\n╱▔▔▏▅▅▅▅▕▔▔╲┈┈┈┈`"
            "`\n▏┈┈╲▂▂▂▂╱┈┈┈▏┈┈┈`"
        )


@register(outgoing=True, pattern="^.nou$")
async def nou(noway):
    if not noway.text[0].isalpha() and noway.text[0] not in ("/", "#", "@", "!"):
        await noway.edit(
            "`\n┈╭╮╭╮\n┈┃┃┃┃\n╭┻┗┻┗╮`"
            "`\n┃┈▋┈▋┃\n┃┈╭▋━╮━╮\n┃┈┈╭╰╯╰╯╮`"
            "`\n┫┈┈  NoU\n┃┈╰╰━━━━╯`"
            "`\n┗━━┻━┛`"
        )

@register(outgoing=True, pattern="^.proo$")
async def nou(noway):
    if not noway.text[0].isalpha() and noway.text[0] not in ("/", "#", "@", "!"):
        await noway.edit(
            "`\n┈╭╮╭╮\n┈┃┃┃┃\n╭┻┗┻┗╮`"
            "`\n┃┈▋┈▋┃\n┃┈╭▋━╮━╮\n┃┈┈╭╰╯╰╯╮`"
            "`\n┫┈┈  Prooooooooooo\n┃┈╰╰━━━━╯`"
            "`\n┗━━┻━┛`"
        )
        
@register(outgoing=True, pattern="^.gm$")
async def nou(noway):
    if not noway.text[0].isalpha() and noway.text[0] not in ("/", "#", "@", "!"):
        await noway.edit(
          "Good Morning"
     )

@register(outgoing=True, pattern="^.ga$")
async def nou(noway):
    if not noway.text[0].isalpha() and noway.text[0] not in ("/", "#", "@", "!"):
        await noway.edit(
          "Good Afternoon"
     )

@register(outgoing=True, pattern="^.ge$")
async def nou(noway):
    if not noway.text[0].isalpha() and noway.text[0] not in ("/", "#", "@", "!"):
        await noway.edit(
          "Good Evening"
     )

@register(outgoing=True, pattern="^.gn$")
async def nou(noway):
    if not noway.text[0].isalpha() and noway.text[0] not in ("/", "#", "@", "!"):
        await noway.edit(
          "Good Night"
     )

@register(outgoing=True, pattern="^.hii$")
async def nou(noway):
    if not noway.text[0].isalpha() and noway.text[0] not in ("/", "#", "@", "!"):
        await noway.edit(
          "Hemlo"
     )
        
        
CMD_HELP.update(
    {
        "memes": ".cowsay\
\nUsage: cow which says things.\
\n\n:/\
\nUsage: Check yourself ;)\
\n\n-_-\
\nUsage: Ok...\
\n\n;_;\
\nUsage: Like `-_-` but crying.\
\n\n.cp\
\nUsage: Copypasta the famous meme\
\n\n.vapor\
\nUsage: Vaporize everything!\
\n\n.str\
\nUsage: Stretch it.\
\n\n.zal\
\nUsage: Invoke the feeling of chaos.\
\n\nOof\
\nUsage: Ooooof\
\n\n.moon\
\nUsage: kensar moon animation.\
\n\n.clock\
\nUsage: kensar clock animation.\
\n\n.hi\
\nUsage: Greet everyone!\
\n\n.coinflip <heads/tails>\
\nUsage: Flip a coin !!\
\n\n.owo\
\nUsage: UwU\
\n\n.react\
\nUsage: Make your userbot react to everything.\
\n\n.slap\
\nUsage: reply to slap them with random objects !!\
\n\n.cry\
\nUsage: y u du dis, i cri.\
\n\n.shg\
\nUsage: Shrug at it !!\
\n\n.run\
\nUsage: Let Me Run, run, RUNNN!\
\n\n.chase\
\nUsage: You better start running\
\n\n.metoo\
\nUsage: Haha yes\
\n\n.mock\
\nUsage: Do it and find the real fun.\
\n\n.clap\
\nUsage: Praise people!\
\n\n.f <emoji/character>\
\nUsage: Pay Respects.\
\n\n.bt\
\nUsage: Believe me, you will find this useful.\
\n\n.pro\
\nUsage: For peru people.\
\n\n.type\
\nUsage: Just a small command to make your keyboard become a typewriter!\
\n\n.lfy <query>\
\nUsage: Let me Google that for you real quick !!\
\n\n.decide [Alternates: (.yes, .no, .maybe)]\
\nUsage: Make a quick decision.\
\n\n.scam <action> <time>\
\n[Available Actions: (typing, contact, game, location, voice, round, video, photo, document, cancel)]\
\nUsage: Create fake chat actions, for fun. (Default action: typing)\
\n\nAnd many more\
\n.nou ; .bot ; .gey ; .gey ; .tf ; .paw ; .taco ; .nih ;\
\n.fag ; .gtfo ; .stfu ; .lol ; .lool ; .fail ; .earth ; .iwi\
\n\n\nThanks to 🅱️ottom🅱️ext🅱️ot (@NotAMemeBot) for some of these."}
)
