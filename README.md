# Shortest-Path-Visualization
This is a project that I made to get a better understanding of the shortest path algorithms and graph theory.

## Current Algorithms 
A* (using Manhattan distance) 
<br />
![A*-demo](https://user-images.githubusercontent.com/33706092/90055347-712bed80-dc9a-11ea-8103-69cc4778440b.gif)
<br />

BFS
<br />
![bfs-demo](https://user-images.githubusercontent.com/33706092/90056172-adac1900-dc9b-11ea-9bc7-8c94fb5b0931.gif)
<br />

## Installation 
1. Clone the repo in a directory 
2. Install the appropriate dependencies:
```bash
pip install -r requirements.txt
```

## Running 
While in the project directory run: 
```bash 
python main.py
```

## Usage 
When the game is launched you can place node by clicking the left mouse button. After the first two node that will be placed are the start (green) and end (red) nodes. After the initial two nodes you user can place barrier (black) nodes. The algorithms will avoid the barrier nodes and seek the end node from the start node. 

Pressing the right mouse button will remove placed nodes. 

Pressing the c key when the algorithm is not running will clear the board.

## License
[MIT](https://choosealicense.com/licenses/mit/)
