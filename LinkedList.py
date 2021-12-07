class Node:
   def __init__(self, val=0):
      self.val = val
      self.next = None

class sLinkedList:
   def __init__(self):
      self.head = None

   def print_list(self):
      cur_node = self.head
      s = ''
      while cur_node:
         if cur_node.val == 0:
            cur_node = cur_node.next
            continue
         s += str(cur_node.val)
         s += ' -> '
         cur_node = cur_node.next

      print(s)

   def find_all_nodes(self):
      cur_node = self.head
      all_nodes = dict()
      while cur_node:
         if cur_node.val is None:
            cur_node = cur_node.next
         all_nodes[cur_node] = cur_node.val
         cur_node = cur_node.next
      return all_nodes

   def find_node(self, val):
      cur_node = self.head
      while cur_node:
         if cur_node.val == 0:
            cur_node = cur_node.next
            continue
         if cur_node.val == val:
            return cur_node
         cur_node = cur_node.next
      return 'Not Found'

   def detect_loop(self):
      temp1 = self.head
      temp2 = self.head
      while temp1 and temp2 and temp2.next:
         temp1 = temp1.next
         temp2 = temp2.next.next
         if temp1 == temp2:
            return 'loop_detected'
      return 'no_loop_detected'

   def num_elements(self):
      cur_node = self.head
      count = 0
      while cur_node:
         count += 1
         cur_node = cur_node.next
      return count
