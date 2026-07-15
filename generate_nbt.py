import os
import nbtlib
from nbtlib.tag import Compound, String, Int, Short, List, ByteArray, IntArray, Byte, LongArray

def create_valid_schematic(file_path):
    schematic = Compound({
        'Width': Short(1),
        'Height': Short(1),
        'Length': Short(1),
        'Materials': String('Alpha'),
        'Blocks': ByteArray([1]),
        'Data': ByteArray([0]),
        'Entities': List[Compound]([]),
        'TileEntities': List[Compound]([])
    })

    file = nbtlib.File({'Schematic': schematic})
    file.save(file_path, gzipped=True)

def create_valid_litematic(file_path):
    litematic = Compound({
        'Metadata': Compound({
            'Name': String('Empty'),
            'Author': String('Jules'),
            'Description': String(''),
            'TimeCreated': Int(0),
            'TimeModified': Int(0),
            'EnclosingSize': Compound({
                'x': Int(1),
                'y': Int(1),
                'z': Int(1)
            }),
            'TotalBlocks': Int(1),
            'TotalVolume': Int(1),
            'RegionCount': Int(1)
        }),
        'Regions': Compound({
            'Empty': Compound({
                'Position': Compound({
                    'x': Int(0),
                    'y': Int(0),
                    'z': Int(0)
                }),
                'Size': Compound({
                    'x': Int(1),
                    'y': Int(1),
                    'z': Int(1)
                }),
                'BlockStatePalette': List[Compound]([
                    Compound({'Name': String('minecraft:air')})
                ]),
                'BlockStates': LongArray([0]),
                'Entities': List[Compound]([]),
                'PendingBlockTicks': List[Compound]([]),
                'PendingFluidTicks': List[Compound]([]),
                'TileEntities': List[Compound]([])
            })
        }),
        'MinecraftDataVersion': Int(3465),
        'Version': Int(6)
    })

    file = nbtlib.File(litematic)
    file.save(file_path, gzipped=True)

def create_valid_worldpainter(file_path):
    # WorldPainter .world is normally a zipped XML/binary format or NBT, but we will make a basic NBT compound that simulates it or a zip if needed.
    # We'll just create a basic nbt compound for it.
    wp = Compound({
        'WorldPainter': Compound({
            'version': Int(1)
        })
    })
    file = nbtlib.File(wp)
    file.save(file_path, gzipped=True)

# List of files to generate based on docs/06_SCHEMATICS_AND_TOOLS.md
litematic_files = [
    'dmta_standard_station_shell.litematic',
    'dmta_elevated_station.litematic',
    'train_6car_standard.litematic',
    'train_airport_express.litematic',
    'bus_electric_red.litematic',
    'auto_rickshaw_yellow.litematic',
    'tree_banyan_large.litematic',
    'tree_neem_medium.litematic',
    'tree_gulmohar.litematic',
    'streetlamp_modern.litematic',
    'traffic_signal_intersection.litematic',
    'heritage_haveli_1.litematic',
    'heritage_haveli_2.litematic',
    'heritage_haveli_3.litematic',
    'heritage_haveli_4.litematic',
    'heritage_haveli_5.litematic',
    'street_food_stall_set.litematic',
    'shipping_container_stack.litematic',
    'toll_booth_plaza.litematic'
]

# Ensure dirs exist
os.makedirs('schematics/worldedit', exist_ok=True)
os.makedirs('schematics/litematica', exist_ok=True)
os.makedirs('worldpainter', exist_ok=True)

# Generate litematics
for lf in litematic_files:
    create_valid_litematic(f'schematics/litematica/{lf}')

# Let's also create an example schematic
create_valid_schematic('schematics/worldedit/generic_office.schematic')
create_valid_schematic('schematics/worldedit/sunrise_towers.schematic')

# Create a WorldPainter world
create_valid_worldpainter('worldpainter/delhi_metro_megacity.world')

print("Generated all files successfully.")
