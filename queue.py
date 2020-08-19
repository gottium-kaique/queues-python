# Queue com Python

from __future__ import annotations
from typing import Any

EMPTY_NODE_VALUE = "__EMPTY_NODE_VALUE__"

class EmpyQueueError(Exception):
  ...

class Node:
  def __init__(self, value: Any) -> None:
    self.value = value
    self.next: Node

  def __repr__(self):
    return f"{self.value}"
    
  def __bool__(self):
    return bool(self.value != EMPTY_NODE_VALUE)


class Queue:
  def __init__(self) -> None:
    self.first: Node = Node(EMPTY_NODE_VALUE)
    self.last: Node = Node(EMPTY_NODE_VALUE)
    self._count = 0

  def push(self, node_value: Any) -> None:
    new_node = Node(node_value)
      if not self.first:
        self.first = new_node

      if not self.last:
        self.last = new_node
      else:
        self.last.next = new_node
        self.last = new_node
    self._count += 1

  def pop(self) -> Node:
      if not self.first:
        raise EmpyQueueError("Empy Queue!")
    first = self.first

      if hasattr(self.first, "next"):
        self.first = self.first.next
      else:
        self.first = Node(EMPTY_NODE_VALUE)
    self._count -= 1
    return first

  def size(self) -> int:
    return self._count

  def __bool__(self) -> bool:
    return bool(self._count)

  def __iter__(self) -> Queue:
    return self
    
  def __next__(self) -> Any:
    try:
        next_value = self.pop()
        return next_value
            
    except EmpyQueueError:
        raise StopIteration

  def __repr__(self) -> str:
    return f"First: {self.first}, Last: {self.last}"

  def empty(self) -> bool:
    return bool(not self._count)

  def front(self):
    return self.first

  def back(self):
    return self.last
