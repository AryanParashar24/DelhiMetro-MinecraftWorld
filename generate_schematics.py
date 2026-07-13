import nbtlib
from nbtlib.tag import *
import os

def create_litematic(filepath, name):
    root = Compound({
        'Metadata': Compound({
            'Name': String(name),
            'Author': String("Delhi Metro Project"),
            'Description': String("Placeholder schematic"),
            'TimeCreated': Long(0),
            'TimeModified': Long(0),
            'TotalBlocks': Int(1),
            'TotalVolume': Int(1)
        }),
        'MinecraftDataVersion': Int(3465),
        'Version': Int(6),
        'Regions': Compound({
            'main': Compound({
                'Position': Compound({'x': Int(0), 'y': Int(0), 'z': Int(0)}),
                'Size': Compound({'x': Int(1), 'y': Int(1), 'z': Int(1)}),
                'BlockStatePalette': List[Compound]([
                    Compound({'Name': String("minecraft:air")}),
                    Compound({'Name': String("minecraft:stone")})
                ]),
                'BlockStates': LongArray([0]),
                'Entities': List[Compound]([]),
                'PendingBlockTicks': List[Compound]([]),
                'PendingFluidTicks': List[Compound]([]),
                'TileEntities': List[Compound]([])
            })
        })
    })
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    nbt_file = nbtlib.File({"": root}, gzipped=True)
    nbt_file.save(filepath, byteorder='big')

def create_schematic(filepath):
    root = Compound({
        'Width': Short(1),
        'Height': Short(1),
        'Length': Short(1),
        'Materials': String("Alpha"),
        'Blocks': ByteArray([1]),
        'Data': ByteArray([0]),
        'Entities': List[Compound]([]),
        'TileEntities': List[Compound]([])
    })
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    nbt_file = nbtlib.File({"Schematic": root}, gzipped=True)
    nbt_file.save(filepath, byteorder='big')

def create_world(filepath):
    root = Compound({
        'version': Int(1),
        'tiles': List[Compound]([])
    })
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    nbt_file = nbtlib.File({"WorldPainter": root}, gzipped=True)
    nbt_file.save(filepath, byteorder='big')

litematics = [
    "dmta_standard_station_shell.litematic",
    "dmta_elevated_station.litematic",
    "train_6car_standard.litematic",
    "train_airport_express.litematic",
    "bus_electric_red.litematic",
    "auto_rickshaw_yellow.litematic",
    "tree_banyan_large.litematic",
    "tree_neem_medium.litematic",
    "tree_gulmohar.litematic",
    "streetlamp_modern.litematic",
    "traffic_signal_intersection.litematic",
    "heritage_haveli_1.litematic",
    "heritage_haveli_2.litematic",
    "heritage_haveli_3.litematic",
    "heritage_haveli_4.litematic",
    "heritage_haveli_5.litematic",
    "street_food_stall_set.litematic",
    "shipping_container_stack.litematic",
    "toll_booth_plaza.litematic"
]

for l in litematics:
    create_litematic(f"schematics/litematica/{l}", l)

create_schematic("schematics/worldedit/sunrise_tower.schematic")
create_schematic("schematics/worldedit/financial_office.schematic")
create_world("worldpainter/delhi_metro.world")
