# conflict-serializable-detector
This is a python script for detecting whether a series of transaction schedule in SQL is conflict-serializable.


A schedule is conflict serializable if it can be transformed into a serial schedule by a series of swappings of adjacent non-conflicting actions.
Through manual check, there are two ways: 
1) go through the whole series of schedule and see whether we can swap the adjacent actions without conflict, if yes then swap, and 
eventually we check whether we can convert the original schedule into a serial schedule, i.e transactions are executed one after the other, in some sequential order.
2) draw the precedence graph and see whether there is a loop in the graph.

Either way is time-consuming, and thus through the script the algorithm could actually test for you, giving you the conclusion of whether the input series of schedules
are conflict-serializable or not.

The script applies a self-defined Graph class as data structure. It applies regular expression to extract different transactions, then construct a Graph and detect whether there is a loop.

Depth First Traversal can be used to detect a cycle in a Graph. DFS for a connected graph produces a tree. There is a cycle in a graph only if there is a back edge, i.e an edge that is from a node to itself (self-loop) or one of its ancestors in the tree produced by DFS, present in the graph. To detect a back edge, keep track of vertices currently in the recursion stack of function for DFS traversal. If a vertex is reached that is already in the recursion stack, then there is a cycle in the tree. 

# To use the script, just git clone the whole directory, cd into the directoy, and then call "python conflict-serializable.py" in the terminal.

It takes the input and then return the decision from the algorithm. 

Demo:
![image](https://user-images.githubusercontent.com/94572804/144966736-a28b5eb3-bb9f-4e47-8e50-a517f9067ef2.png)


