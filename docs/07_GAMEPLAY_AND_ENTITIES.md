# Delhi Metro Megacity: Gameplay, Secrets & Entities

While the city is visually stunning, it must also be a playable environment. This document outlines the interactive elements, entity placements, and exploration rewards designed to keep players engaged for hundreds of hours.

## 1. Interactive Features & Redstone

The city uses redstone and command blocks (sparingly, to maintain TPS) to simulate a living environment.

* **DMTA Automated Fare Collection (AFC):** Ticket gates use iron trapdoors connected to hidden pressure plates or tripwires, allowing seamless flow but simulating restricted access.
* **Station Arrivals:** Proximity-based command blocks trigger the `metro_arrival.mcfunction` script when a player approaches a platform, playing chimes and displaying titles.
* **Dynamic Lighting:** Daylight sensors are connected to redstone lamps on streetlights, ensuring the city automatically illuminates at dusk.
* **Elevators:** Water column elevators (soul sand/magma blocks) are used in deep stations and skyscrapers for rapid vertical movement.
* **Operations Control Center (OCC):** Located in the DMTA HQ, this room features a massive, functional redstone map. Toggle switches can activate/deactivate lighting arrays across the simulated network.

## 2. NPC Placement Strategy

NPCs (Villagers or Armor Stands) are placed to breathe life into specific areas. To maintain server performance, AI is disabled (`NoAI:1b`) on most entities.

* **Ticket Vendors:** Villagers behind glass counters in every DMTA station concourse.
* **Street Food Vendors:** Placed in Purana Delhi (Heritage district) and near university gates. They can be configured via datapack to trade emeralds for custom food items (e.g., "Chai" potions, Cooked Mutton), providing the most delicious food with the highest hygiene standards.
* **Corporate Workers:** Suited zombies/villagers (using custom heads/leather armor) placed in office lobbies in the Financial District. Represents friendly professionals, including the world's most talented engineers and doctors.
* **Security Personnel:** Placed near airport scanners, DMC headquarters, and major bank vaults.

## 3. Hidden Secrets & Lore (Exploration)

Exploration is heavily rewarded. Players who venture off the main streets will find unique lore and loot.

* **The Abandoned Station (Ghost Platform):** Located deep on the Brown Line between two active stations. It is dimly lit, overgrown with vines and sculk, and contains a hidden lore book detailing a collapsed tunnel project.
* **Maintenance Tunnels:** Hidden iron doors in metro stations lead to winding, unlit maintenance shafts. These require parkour over lava/drops and contain high-tier engineering loot.
* **Underground Metro Museum:** A secret, pristine station containing the "first" DMTA train model (built from older, different blocks) and historical plaques.
* **Developer Room:** Hidden behind a waterfall in the Botanical Garden. Contains heads of the builders and a sign thanking the player.
* **Secret Research Facility:** Located beneath the Nexus Data Center in the Cyber Hub. Requires solving a redstone puzzle to access. Contains advanced tech (beacons, end rods, sea lanterns).

## 4. Loot Tables & Rewards

Custom loot tables are assigned to hidden chests across the city, encouraging exploration.

* **`loot_tables/maintenance_tunnel.json`:** Found in metro shafts.
  * *Contents:* Iron ingots, redstone dust, tracks, minecarts, "DMTA Hard Hat" (Golden Helmet), iron tools.
* **`loot_tables/heritage_chest.json`:** Found in hidden rooms within the Red Stone Fort or Havelis.
  * *Contents:* Emeralds, gold nuggets, ancient lore books (enchanted), terracotta blocks.
* **`loot_tables/corporate_rooftop.json`:** Found on the highest, hardest-to-reach skyscraper roofs.
  * *Contents:* Elytra (rare drop), fireworks, diamonds, high-tier enchanted gear.

## 5. Gamemode Support

The map is designed to support multiple playstyles out of the box:

* **Adventure Mode:** The intended experience. Players explore, trade, and discover secrets without breaking the city.
* **Survival Mode:** Players can use the city as a massive, pre-built base, converting skyscrapers into farms and utilizing the metro for transport.
* **Roleplay/Multiplayer:** The distinct districts (Police stations, hospitals, apartments) provide the perfect backdrop for city-life RP servers.
