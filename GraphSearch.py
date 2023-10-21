class Node:
  def __init__(self, childNodes,     index):
    self.childNodes = childNodes 
    self.index = index

class GoalNode:
  def __init__(self, index):
    self.index = index

node5 = GoalNode(4)
node4 = Node([node5], 3)
node3 = Node(None,2)
node2 = Node([node3, node4], 1)
node1 = Node([node2], 0)

Frontier = []

def StackSearch():
  Frontier.append(node1)
  while len(Frontier) > 0:
    node = Frontier.pop()
    if node.index == 4:
      print("Found")
      return
    for child in node.childNodes:
      Frontier.append(child)

StackSearch()




    


