import re

with open("README.md", "r") as f:
    readme = f.read()

index = """- [01_BUILD_PLAN_AND_PHASES](docs/01_BUILD_PLAN_AND_PHASES.md)
- [02_DISTRICT_LAYOUT](docs/02_DISTRICT_LAYOUT.md)
- [03_METRO_NETWORK_AND_STATIONS](docs/03_METRO_NETWORK_AND_STATIONS.md)
- [04_TERRAIN_AND_LANDSCAPING](docs/04_TERRAIN_AND_LANDSCAPING.md)
- [05_PALETTES_AND_MATERIALS](docs/05_PALETTES_AND_MATERIALS.md)
- [06_SCHEMATICS_AND_TOOLS](docs/06_SCHEMATICS_AND_TOOLS.md)
- [07_GAMEPLAY_AND_ENTITIES](docs/07_GAMEPLAY_AND_ENTITIES.md)
- [08_LIGHTING_AND_OPTIMIZATION](docs/08_LIGHTING_AND_OPTIMIZATION.md)"""

readme = re.sub(r'The master design documentation is organized into specialized markdown files detailing various aspects of the project:\n\n.*?\n\n## Datapack', f'The master design documentation is organized into specialized markdown files detailing various aspects of the project:\n\n{index}\n\n## Datapack', readme, flags=re.DOTALL)

with open("README.md", "w") as f:
    f.write(readme)
