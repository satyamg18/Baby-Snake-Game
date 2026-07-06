# 🐍 Baby Snake Game

A classic Snake game built with **Python**, developed as the final project for **Stanford University's Code in Place** program. The snake navigates a 400×400 canvas, chases randomly placed food, and must stay within the walls.

---

## 🎓 About Code in Place

This project was built during **[Code in Place](https://codeinplace.stanford.edu)** - a free, 6-week online introductory Python programming course offered by **Stanford University**.

- 📚 Based on the first half of Stanford's **CS106A** - one of the world's most renowned intro CS courses
- 🌍 Open to absolute beginners globally, with no prior coding experience required
- 👩‍🏫 Features live small-group sections led by volunteer section leaders from around the world
- 🏆 Students complete creative projects - this Snake game is the final portfolio project of the course
- 🎓 Participants receive a **Certificate of Completion** from Stanford upon finishing

> *"Code in Place is a community-powered, Stanford-quality programming education - free for everyone."*

---

## 🎮 How It Works

- The snake starts at position `(0, 0)` on a 400×400 canvas
- Move using the **Arrow Keys** - the snake only moves when a key is pressed
- A red **goal** spawns at a random position on the canvas
- When the snake reaches the goal, it **scores** and the goal **teleports** to a new random location
- The snake is contained within the walls - it stops at the boundary

---

## 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core language |
| `graphics` (Canvas) | Stanford CS106A visual library for 2D canvas rendering |
| `random` | Random food position generation |
| `time` | Game loop timing and delay control |

---

## ▶️ Running the Game

> ⚠️ **Important:** This project uses Stanford's `graphics` (Canvas) library, which is **built into the Code in Place online environment** and is not available as a standard pip package. It cannot be run as a standalone script without that environment.

### Option 1 - Run in Stanford's Code in Place IDE *(Recommended)*
1. Enroll in [Code in Place](https://codeinplace.stanford.edu) (free, offered annually by Stanford)
2. Open the online coding environment
3. Paste the contents of `snake_game.py` into the editor
4. Click **Run**

### Option 2 - Run locally with the CS106A graphics library
The Stanford `graphics.py` library can be obtained from the [CS106A course materials](https://cs106a.stanford.edu). Place `graphics.py` in the same directory as `snake_game.py`, then:

```bash
git clone https://github.com/satyamg18/Baby-Snake-Game.git
cd Baby-Snake-Game

# Place graphics.py from CS106A here, then:
python snake_game.py
```

---

## 📚 What I Learned

Through the Code in Place curriculum and this project, I developed:

- 🔁 **Game loops** - using `time.sleep()` to control frame rate
- 🎨 **Canvas rendering** - drawing and moving rectangles on a 2D grid
- 💥 **Collision detection** - detecting wall and self-collision
- 🎲 **Randomness** - spawning food at unpredictable positions
- ⌨️ **Keyboard input** - real-time directional control
- 🧱 **Boundary logic** - keeping the snake constrained within canvas walls

---

## 📜 License

MIT - feel free to learn from or build on this project.
