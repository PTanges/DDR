# Technical Document: Game Structure

### Game Structure:

Game Initialization
- > Init Pygame
  > - Read stats from save file for songs (or at the end of the song)
  > - Define Colours by R G B, global?
  > - Define Key Mapping (WASD, ASDF, QWER, or Arrow Keys or ALL)
  > - Define Note Properties (Speed, L/W by sprite size, position by Screen Dimensions)
  > - Resources:
  > - Link 01 - <https://www.pygame.org/docs/>
  > - Link 02 - <https://www.pygame.org/docs/ref/pygame.html>

Start Screen
- > Song Selection (1) via button(s)
  > 
  > In-Game Credits
  > 
  > Quit Game

Song Data:
- > Song Pre Start:
  > - Limit Framerate to a music metric (60 fps)
  > - Define Arrow Paths (Keypressdown)
  > - Developer defined Unique Song Beatmap
  > - - Technical (Coordinates): Center Screen +/- distance, then distance + beat.width
  > - - Technical (Data Structure): May Int Array with "time" to next beat x4
  > - - Con: Large storage structure + tedious implementation
  > - - Technical (Data Structure): May Int Array with bools per song length x BPM
  > - - Pro: More direct song editing
  > - - Con: LARGER storage structure. 3 min song with 140 bpm is 420 indexes PER arrow key
- > Song Start:
  > - Read from US Beatmap
  > - Begin Timer/Clock & Play Song
  > - Spawn beats in synch with Clock & Beatmap
  > - - Spritegroup add (ARROW-KEY)
  > - - Upon keypress measure distance for score. No overlap but will have boundary for miss
  > - - {Miss, Good, Great, Perfect} based on +/- Y distance. After passing, less distance leniency + will prioritize INCOMING keys (ex: 8:2 frame timing ratio)
  > - - Score & streak increases per "correct" input
  > - - Technical: (1) or (4) Spritegroups
  > - - T!Implement (4) Pros: May be easier to implement beat check on keydown instead of reading the ENTIRE (1) sprite group
- > Song Complete:
  > - Read save file for previous stats.
  > - - New high score? New highest streak?
  > - - Data Validation: In case of external tampering, ignore/overwrite save file
  > - - Technical: XML File. Store values as integers. Todo: Research compatability with Python
  > - New Screen: Score shown!
  > - Stats: Misses, Goods, Greats, Perfects
  > - Longest Streak
  > - Accuracy (%):
  > - - (Perfect.count + Great.count + Good.count) / Beatmap.PerfectQuantity as a %
  > - - Assign an integer value per score. Hit count becomes a % relative to "all perfects." Due to formula, can't have > 100%
  > - - ie. Perfect = 100, then a Good of 10 means all key hits being goods = 10% accuracy
  > - - Source: OSU
  > - - Perfect = 100
  > - - Great = 75
  > - - Good = 25
  > - - Miss = 0 (derived by Beatmap.quantity - P.count - Gr.count - Go.count = Miss.count)
  > - Write stats to save file
  > - Button to return to Track Selection / Quit Game

Development Checklist:
- > Software (Technical):
  > - Pygame
  > - Git + Github
  > - IDE (Python)
  > 
  > Game Assets:
  > - Soundtracks (Public Domain / Royalty Free Music), "Tracks"
  > - - Suggested Genres: Pop, Jpop, Rock, Alt Rock, Metal, EDM
  > - Beat per direction (Left, Up, Right, Down) => (4)
  > - Text (Miss, Good, Great, Perfect)

Visuals
- > By Screen (Track Selection):
  > - Top Left: Track Composer (& Difficulty)
  > - Center Left: Track Name
  > - Bottom Right: Quit Button
  > 
  > By Screen (Song In Progress):
  > - Top Left: Song Name (& Difficulty)
  > - Top Right: Song Accuracy by % (:.2f)
  > - Center Column(s): Notes & Note-paths
  > - Center Column: Note accuracy text & Current Combo (Over/under notes)
  > 
  > By Screen (Results Screen):
  > - Top Left: Song Name (& Difficulty)
  > - Center: Stacked stats for PGGM
  > - Center Right: Accuracy by %
  > - Center Bottom: Return to Track List, Quit


Key / Terminology:
- > Rhythm Game Terms:
  > - Songs: Songs / Tracks
  > - Beats: Notes (from a Beatmap)
  > - Beatmap: Think of a music score / music sheet

State Flow Diagram:
- > Technical: State Machine
  > - START -> Selection -> Play -> Results -> Selection || Exit
  > - ... Selection -> Credits -> Selection
  > - ... Selection -> Quit
![Rhythm Game - State Machine Diagram.png](Rhythm%20Game%20-%20State%20Machine%20Diagram.png)
  > - - State Machine Diagram, states separated by "screens"

Referenced Games
- OSU (Desktop)
- Rhythm Heaven (Console)
- Deemo (Mobile)
- Guitar Hero (Arcade)
- Dance Dance Revolution (Arcade)
- Taiko (Arcade)