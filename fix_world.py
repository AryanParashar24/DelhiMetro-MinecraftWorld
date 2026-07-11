import nbtlib
from nbtlib.tag import *

root = Compound({
    "WorldPainterVersion": Int(1)
})
file = nbtlib.File({"": root})
file.gzipped = True
file.save("worldpainter/delhi_metro_6000x6000.world")
