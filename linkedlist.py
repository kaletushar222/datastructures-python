class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next

	def append(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		lastnode = self.head
		while lastnode.next:
			lastnode = lastnode.next

		lastnode.next = new_node

	def prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insert_after_node(self, prev_node, data):
		if not prev_node:
			print('Previous node not found') 
		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def delete_node(self, key):
		cur_node = self.head
		
		if cur_node and cur_node.data == key:
			self.head = cur_node.next
			cur_node = None
			return

		prev_node = None
		while cur_node.data != key:
			prev_node = cur_node
			cur_node = cur_node.next

		if cur_node is None:
			return

		prev_node.next = cur_node.next
		cur_node = None

	def delete_node_at_pos(self, pos):
		cur_node = self.head

		if cur_node and pos == 1:
			self.head = cur_node.next
			cur_node = None
			return

		count = 1
		prev_node = None
		while cur_node and pos != count:
			prev_node = cur_node
			cur_node = cur_node.next
			count+=1

		if cur_node is None:
			return

		prev_node.next = cur_node.next
		cur_node = None

	def len_iterative(self):
		cur_node = self.head
		count = 0
		
		while cur_node:
			cur_node = cur_node.next
			count+=1

		return count

	def len_recursive(self, node):
		if node is None:
			return 0
		return 1 + self.len_recursive(node.next)

llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
#print(llist.len_iterative())
print(llist.len_recursive(llist.head))
#llist.delete_node('A')
#llist.delete_node_at_pos(1)
#llist.prepend('E')
#llist.prepend('F')


#llist.insert_after_node(llist.head.next, "x")
#llist.print_list()
