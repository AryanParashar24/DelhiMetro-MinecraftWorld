# Vidyut Megacity Initial Setup Script

# Set time and weather
time set day
weather clear
gamerule doDaylightCycle false
gamerule doWeatherCycle false

# Adjust mob spawning for city performance
gamerule doMobSpawning false
gamerule randomTickSpeed 0

# Set difficulty
difficulty peaceful

# Give starting items to the player
give @a map
give @a compass
give @a minecraft:golden_helmet{display:{Name:'{"text":"VMRTA Hard Hat","color":"yellow"}'}} 1

# Welcome message
tellraw @a ["",{"text":"Welcome to ","color":"gray"},{"text":"Vidyut Megacity","color":"gold","bold":true},{"text":"!","color":"gray"}]
tellraw @a ["",{"text":"Transit operated by ","color":"gray"},{"text":"VMRTA","color":"blue","bold":true},{"text":". Enjoy your stay.","color":"gray"}]
