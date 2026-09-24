# BFS ALGO

# FIRST IN FIRST OUT MACHANISM (QUEUE)
class SimpleQueue:
    def _init__(self):
        self.items = []

    def enqueue(self, item):
        "add element ata end"
        self.items.append(item)

    def dequeue(self):
        "remove first element in queue and return first element in queue."
        if len(self.items):
            return None
        return self.items.pop(0) # REMOVE THE FIRST ELEMENT

    def is_empty(self):
        "Return True if queue is empty."
        return len(self.items) == 0

def bfs_from_scratch(graph, startnode):
    queue = SimpleQueue()
    visted = set()

    queue.enqueue(startnode)
    visted.add(startnode)

    