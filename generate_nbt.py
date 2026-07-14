import nbtlib
from nbtlib.tag import Compound, String, Int, List, Byte, ByteArray, LongArray
import os

os.makedirs('schematics/worldedit', exist_ok=True)
os.makedirs('schematics/litematica', exist_ok=True)
os.makedirs('worldpainter', exist_ok=True)

# Litematic schema requires some basic stuff
litematic = nbtlib.File({
    'Metadata': Compound({
        'Author': String('Jules'),
        'Description': String(''),
        'EnclosingSize': Compound({'x': Int(1), 'y': Int(1), 'z': Int(1)}),
        'Name': String('placeholder'),
        'RegionCount': Int(1),
        'TimeCreated': Int(0),
        'TimeModified': Int(0),
        'TotalBlocks': Int(1),
        'TotalVolume': Int(1)
    }),
    'Regions': Compound({
        'placeholder': Compound({
            'BlockStates': LongArray([0]),
            'BlockStatePalette': List[Compound]([Compound({'Name': String('minecraft:air')})]),
            'Entities': List[Compound]([]),
            'PendingBlockTicks': List[Compound]([]),
            'PendingFluidTicks': List[Compound]([]),
            'Position': Compound({'x': Int(0), 'y': Int(0), 'z': Int(0)}),
            'Size': Compound({'x': Int(1), 'y': Int(1), 'z': Int(1)}),
            'TileEntities': List[Compound]([])
        })
    }),
    'MinecraftDataVersion': Int(3465),
    'Version': Int(6)
})
litematic.save('schematics/litematica/placeholder.litematic', gzipped=True)

schematic = nbtlib.File({
    'Width': Int(1),
    'Height': Int(1),
    'Length': Int(1),
    'Materials': String('Alpha'),
    'Blocks': ByteArray([0]),
    'Data': ByteArray([0]),
    'Entities': List[Compound]([]),
    'TileEntities': List[Compound]([])
})
schematic.save('schematics/worldedit/placeholder.schematic', gzipped=True)

world = nbtlib.File({
    'WorldPainter': String('Placeholder')
})
world.save('worldpainter/placeholder.world', gzipped=True)

print("NBT generated successfully.")
