class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None:
    if not self.head:
      self.head = self.last = Node(data)
    else:
      node = Node(data)
      self.last.next = node
      self.last = node

  def dequeue(self) -> None:
    if not self.head:
      return
    else:
      temp = self.head
      self.head = self.head.next
      return temp

  def status(self) -> None:
    temp = self.head
    while temp:
      print(temp.data,end="=>")
      temp = temp.next
    print(temp)


# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
