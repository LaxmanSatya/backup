# implementaition of queue
class simple_queue:
    def __init__(self):
        self.items = []

    # add new element to queue
    def enqueue(self, item):
        self.items.append(item)

    # removeing items at strating... and return that visited element.
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    # checking is any in queue
    def is_empty(self):
        return len(self.items) == 0


def _algo_bfs(graph, startnode):
    #  for queue
    queue = simple_queue()
    # visted purpose
    visted = list()

    # append new node to queue ata end
    queue.enqueue(startnode)

    # add same node to visted
    visted.append(startnode)

    # print action perform for initalize Breadth-first-search
    print("BFS Traversal Order", end = " ")

    # core one
    # if queue haved no nodes not enter to this loop
    while not queue.is_empty():
        current_node = queue.dequeue()
        print(current_node, end=" ")

        for neighbor in graph[current_node]:
            if neighbor not in visted:
                visted.append(neighbor)
                queue.enqueue(neighbor)
            

print() # new line purpose