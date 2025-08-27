# CSE423_Game-Project
Meowgic Catch is a game build on Python OpenGL
# 🐾 Meowgic Catch

> A 3D grid-based arcade game where a shape-built cat dashes around collecting fish, outsmarting dogs, and adapting to shifting weather and skies.

---

- **Project Overview**  
  Meowgic Catch is a **3D grid-based game** where you control a cat made from simple shapes. You’ll collect fish, dodge enemy dogs, and leverage time-limited boosts. The environment evolves as you play—**sky cycles** and **random weather** change how you move and plan.

- **Objective**  
  **Collect as many fish as possible** while staying alive. Use movement, jumps, combos, decoys, and meows to evade dogs, intercept stolen fish, and maximize your score before your lives run out.

- **Game Features**  
  - **Player Movement**: Move and rotate the cat on the grid.  
  - **Jump Action**: Leap briefly to avoid obstacles or enemies.  
  - **Cheat Mode**: Auto-collect nearby fish in a circular path.  
  - **Pounce Combo**: Jump and grab multiple fish mid-air for bonus value.  

- **Fish Types**  
  - **Normal Fish**: Spawn at random grid positions.  
  - **Power-Up Fish** (glowing gold): Grants **Speed Boost** or **Double Score** for **10s**.  
  - **Fast Fish**: Move quickly—requires sprinting/timing to catch.  
  - **Timed Fish**: Disappear after a short window—reach them fast.

- **Enemy Behaviors**  
  - **Enemy Dogs**: Spawn and **chase** the cat.  
  - **Enemy Collision**: Contact with a dog **reduces a life**.  
  - **Dog Block/Steal**: Dogs can **steal nearby fish**; intercept to recover momentum.  
  - **Chase Diversion**: Drop a **decoy fish** to distract dogs for **5s**.

- **Abilities & Systems**  
  - **Meow Scare**: Stun nearby dogs for **2s** (cooldown-based).  
  - **Score System**: Collecting fish increases score; power-ups amplify gains.  
  - **Life System**: Start with **5 lives** (configurable).  
  - **Restart Game**: Resets lives, score, environment, and spawns.

- **Dynamic Environment**  
  - **Sky Cycle**: Every **30s** the scene transitions (**Morning → Afternoon → Evening**).  
  - **Weather Shifts**:  
    - 🌧️ **Rain** → Slippery ground (reduced traction/longer slide).  
    - 🌫️ **Fog** → Reduced visibility (shorter sight/indicator range).

---

- **Suggested Controls**  
  - **Move/Rotate**: WASD / Arrow Keys  
  - **Jump**: Space  
  - **Pounce Combo**: Space while moving over fish clusters  
  - **Cheat Mode**: C (toggle if enabled)  
  - **Meow Scare**: M (cooldown)  
  - **Drop Decoy**: Q  
  - **Restart**: R  
  > _Customize these in your input settings; names here are placeholders._

- **Gameplay Tips**  
  - **Chain pounces** during power-up windows to snowball score.  
  - **Use decoys** to split dog packs before diving into crowded fish lanes.  
  - **Track weather**: brake earlier in rain; navigate by minimap cues in fog.  
  - **Time-limited fish**: prioritize them over distant static fish.

---

- **Project Structure (Example)**  
MeowgicCatch/
├─ Assets/ # Models, sprites, audio, VFX
├─ Scripts/ # Gameplay systems (movement, AI, spawns)
├─ Scenes/ # Main scene(s)
├─ Settings/ # Input, quality, physics configs
└─ README.md





