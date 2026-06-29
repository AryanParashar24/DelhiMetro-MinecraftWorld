# Metro Arrival Announcement Script
# Can be triggered by command blocks at stations

# Play arrival chime
playsound minecraft:block.note_block.chime master @a[distance=..50] ~ ~ ~ 1 1
playsound minecraft:block.note_block.chime master @a[distance=..50] ~ ~ ~ 1 1.2
playsound minecraft:block.note_block.chime master @a[distance=..50] ~ ~ ~ 1 1.5

# Display title to nearby players
title @a[distance=..50] times 10 60 10
title @a[distance=..50] subtitle {"text":"Please stand clear of the doors.","color":"gray","italic":true}
title @a[distance=..50] title {"text":"Train Arriving","color":"yellow","bold":true}

# Chat announcement
tellraw @a[distance=..50] ["",{"text":"[VMRTA] ","color":"blue","bold":true},{"text":"A train is now arriving at this station. Please allow passengers to exit before boarding.","color":"white"}]
