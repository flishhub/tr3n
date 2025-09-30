# tr3n
Tron Light Cycle Clon3

# Tr3n Light Cycle 🌀

Tr3n Light Cycle is a fast-paced, Tron-inspired arcade game built in Python with Pygame. Designed for modular expansion and creative polish, it features:

- ⚔️ Local multiplayer light cycle battles 
- 🧠 AI opponent logic (coming soon)
- 🎮 Custom menu systems and game states
- 🧩 Clean, scalable class architecture
- 🔐 Optional secure compute themes woven into gameplay (coming soon)

Whether you're chasing nostalgia or building your Python portfolio, Tr3n offers a sleek foundation for arcade-style experimentation. Contributions, forks, and feature ideas are welcome—this is a living project with plenty of room to grow.

> Built by John Flisher. Co-designed by Paul Flisher. Modular by design. Fun by necessity.
>
> ## Version History 📜



---

## 🕹️ TR3N Light Cycle – v1.6


### 🚀 Features

- **Classic Grid Play**: No boundary enforcement, pure arcade movement
- **Modular Menu System**: Choose between Start Game, Best of 3, Flynn Lives, or Quit
- **Audio Greeting**: “Greetings, programs” plays on launch (customizable)
- **Scoreboard**: Tracks wins per round, displayed during gameplay
- **Best of 3 Mode**: Optional match logic with round tracking and final winner display
- **Flynn Lives Terminal**: Mythic overlay with ENCOM messages and lore expansion

---

### 🎮 Controls

**Player 1**  
- Up: `W`  
- Down: `S`  
- Left: `A`  
- Right: `D`

**Player 2**  
- Up: `↑`  
- Down: `↓`  
- Left: `←`  
- Right: `→`

---

### 📁 File Structure

```
TR3N/
├── main.py               # Game loop and menu logic
├── Player.py             # Player movement and trail logic
├── Menu.py               # Menu rendering and input
├── assets/
│   └── audio/
│       └── greetings_programs.wav
```

---

### 🧪 Requirements

- Python 3.8+
- Pygame (`pip install pygame`)
- Optional: audio file in `assets/audio/greetings_programs.wav`

---

### 🧠 Lore Integration

TR3N v1.6 includes a Flynn Lives terminal overlay, accessed via the menu. It simulates ENCOM shell access, Grid node connection, and Alan Bradley’s mythic message:  
> “The Grid is real. Flynn was right.”

This sets the stage for future TRON: Ares-inspired expansions.

---

### 📦 Distribution Notes

TR3N v1.5 is deprecated and not publicly available. v1.6 is the current public-facing build. Future versions may include:

- Multiplayer grid logic  
- AI commentary (Cortana-inspired)  
- Cloud-hosted launcher  
- Legacy Mode unlocks

---





>
 ### v1.3 – Multiplayer & Menu Expansion
- Two-player local mode with split keyboard controls - Ready Player 2
- Independent light cycle instances and trails
- Collision detection between players and screen boundaries
- Modular menu system integrated into game loop
- Modualr Player library added


### v1.0 – Core Foundations 9-4-25
- 🚀 Basic light cycle movement and collision detection
- 🧱 Single-player mode with simple game loop
- 🧼 Clean menu system with start/quit functionality
- 🧪 Modular class structure for easy expansion

This initial release laid the groundwork for Tr3n’s arcade feel and modular design. No multiplayer, no AI—just the raw mechanics and a clean slate for future growth.
