# ai-projects

## TIC-TAC-TOE  
Brainstorm Tic Tac Toe function adjustments

- Non negative reward is given after the game ends (except for draw)
- Q updates not performed at every action step but after the end of the game
- Q updates is performed by propagating its new value from the last move backward to the first move
- update formula has to also account for opponent moves through out the game

### Breakdown of the QValue Array
```
QValues [
    [   state = 0,Y
    [QVs],  state = 0,0
    [QVs],  state = 0,1
    [QVs],  state = 0,2
    [QVs],  state = 0,3
     ...,   state = 0,N
    ],
    [   state = 1,Y
    [QVs],  state = 1,0
    [QVs],  state = 1,1
    [QVs],  state = 1,2
    [QVs],  state = 1,3
    ],
    ...,
    ]
### QVs = [north_val, south_val, east_val, west_val]
```

## Resources

https://www.youtube.com/watch?feature=player_embedded&v=hsz0zq6AXGE  

https://www.youtube.com/watch?feature=player_embedded&v=R0vTZp0ve4s  

http://ai.berkeley.edu/reinforcement.html

## Maze Solution Instructions

Download qLearningAgents.py

Replace the existing reinforcement/qLearningAgents.py with the file you just downloaded

run `/path/to/python /path/to/gridworld.py -a q -k 100`
