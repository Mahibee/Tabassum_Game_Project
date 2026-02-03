# CSE423 Game Project – Meowgic Catch 🎮🐾

**Meowgic Catch** is a 3D arcade-style computer graphics game built using **Python and OpenGL**.  
The game features a shape-built cat navigating a dynamic grid-based world, collecting fish, avoiding enemy dogs, and adapting to changing environments.

---

## 🐾 Meowgic Catch

A 3D grid-based arcade game where a shape-built cat dashes around collecting fish, outsmarting dogs, and adapting to shifting weather and skies.

---

## 📌 Project Overview

Meowgic Catch is a **3D grid-based game** where the player controls a cat constructed from simple geometric shapes.  
The objective is to collect fish, avoid or outmaneuver enemy dogs, and strategically use abilities and power-ups.

The environment evolves as gameplay progresses:
- Sky cycles through different times of day
- Random weather effects alter movement and visibility

---

## 🎯 Objective

Collect as many fish as possible while staying alive.

- Dodge enemy dogs
- Use jumps, combos, decoys, and special abilities
- Maximize score before all lives are lost

---

## 🕹️ Game Features

### Player Movement
- Move and rotate the cat on a grid-based map
- Smooth directional control and rotation

### Jump Action
- Jump to avoid obstacles or enemies
- Used for traversal and combo actions

### Cheat Mode
- Automatically collect nearby fish in a circular radius

### Pounce Combo
- Jump and collect multiple fish mid-air
- Grants bonus score for skillful timing

---

## 🐟 Fish Types

- **Normal Fish**  
  Spawn randomly on the grid

- **Power-Up Fish (Glowing Gold)**  
  Grants **Speed Boost** or **Double Score** for 10 seconds

- **Fast Fish**  
  Move quickly and require precise timing to catch

- **Timed Fish**  
  Disappear after a short duration—must be collected quickly

---

## 🐕 Enemy Behaviors

- **Enemy Dogs**  
  Spawn and actively chase the cat

- **Enemy Collision**  
  Contact with a dog reduces one life

- **Dog Block / Steal**  
  Dogs can steal nearby fish—intercept them to regain advantage

- **Chase Diversion**  
  Drop a decoy fish to distract dogs for 5 seconds

---

## ✨ Abilities & Systems

- **Meow Scare**  
  Stuns nearby dogs for 2 seconds (cooldown-based)

- **Score System**  
  Collecting fish increases score; power-ups amplify gains

- **Life System**  
  Player starts with **5 lives** (configurable)

- **Restart Game**  
  Resets lives, score, environment, and spawns

---

## 🌦️ Dynamic Environment

### Sky Cycle
- Changes every 30 seconds  
  *(Morning → Afternoon → Evening)*

### Weather Effects
- 🌧️ **Rain** – Slippery ground, reduced traction
- 🌫️ **Fog** – Reduced visibility and shorter detection range

---

## 🎮 Suggested Controls

| Action | Key |
|------|----|
| Move / Rotate | WASD / Arrow Keys |
| Jump | Space |
| Pounce Combo | Space (while moving over fish clusters) |
| Cheat Mode | C (toggle) |
| Meow Scare | M |
| Drop Decoy | Q |
| Restart Game | R |

> Controls can be customized in the input settings.  
> Key bindings listed here are default placeholders.

---

## 💡 Gameplay Tips

- Chain pounce combos during power-up windows to maximize score
- Use decoys to split dog packs before entering dense fish zones
- Adjust movement during rain to avoid slipping
- In fog, rely on minimap cues and close-range indicators
- Prioritize time-limited fish over distant static ones

---

## 📂 Project Structure (Example)

MeowgicCatch/
├─ Assets/ # Models, sprites, audio, visual effects
├─ Scripts/ # Gameplay systems (movement, AI, spawning)
├─ Scenes/ # Main game scenes
├─ Settings/ # Input, physics, and quality configurations
└─ README.md


---

## 👤 Author

**Tabassum Mahin**  
CSE423 – Computer Graphics Project  
Built using **Python + OpenGL**




