import nbtlib
from nbtlib.tag import Compound, String, Int, List, Byte
import os

litematica_schematics = [
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

def create_dummy_litematic(filepath):
    # Create a basic litematica structure to be a valid NBT
    file = nbtlib.File({
        'Metadata': Compound({
            'Name': String(os.path.basename(filepath)),
            'Author': String('Delhi Metro Megacity Builder'),
            'Description': String('Dummy Schematic for scaffolding')
        }),
        'Regions': Compound({
            'DummyRegion': Compound({
                'Size': Compound({
                    'x': Int(1), 'y': Int(1), 'z': Int(1)
                }),
                'BlockStates': nbtlib.tag.LongArray([0]),
                'BlockStatePalette': List[Compound]([
                    Compound({'Name': String('minecraft:air')})
                ])
            })
        })
    })
    file.save(filepath, gzipped=True) # Litematica files are usually gzipped NBT

def create_dummy_schematic(filepath):
    # Create a basic worldedit schematic structure
    file = nbtlib.File({
        'Width': Int(1),
        'Height': Int(1),
        'Length': Int(1),
        'Materials': String('Alpha'),
        'Blocks': nbtlib.tag.ByteArray([0]),
        'Data': nbtlib.tag.ByteArray([0]),
        'Entities': List[Compound]([]),
        'TileEntities': List[Compound]([])
    })
    file.save(filepath, gzipped=True)

def create_dummy_world(filepath):
    # Just an empty compound for WorldPainter
    file = nbtlib.File(Compound({}))
    file.save(filepath, gzipped=False) # WorldPainter files are often not gzipped in some forms, or use custom binary

os.makedirs('schematics/litematica', exist_ok=True)
for name in litematica_schematics:
    create_dummy_litematic(f'schematics/litematica/{name}')

os.makedirs('schematics/worldedit', exist_ok=True)
create_dummy_schematic('schematics/worldedit/sunrise_towers.schematic')
create_dummy_schematic('schematics/worldedit/generic_office.schematic')

os.makedirs('worldpainter', exist_ok=True)
create_dummy_world('worldpainter/delhi_metro_megacity.world')

print("Created dummy NBT files.")
