"""Add two numbers represented by reversed linked lists."""


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def __repr__(self):
		return f"Node({self.value})"


# UPI Steps:
# U - Understand: the digits are stored in reverse order in two linked lists.
# P - Plan: add node values one by one, keeping track of carry.
# I - Implement: build a new linked list with each resulting digit.


def add_two_numbers(head_a, head_b):
	dummy_head = Node(0)
	current = dummy_head
	carry = 0

	while head_a is not None or head_b is not None or carry:
		total = carry

		if head_a is not None:
			total += head_a.value
			head_a = head_a.next

		if head_b is not None:
			total += head_b.value
			head_b = head_b.next

		carry = total // 10
		current.next = Node(total % 10)
		current = current.next

	return dummy_head.next


def print_list(head):
	values = []
	while head is not None:
		values.append(str(head.value))
		head = head.next
	print(" -> ".join(values))


if __name__ == "__main__":
	# list 1: 2 -> 4 -> 3 (342)
	# list 2: 5 -> 6 -> 4 (465)
	head_a = Node(2, Node(4, Node(3)))
	head_b = Node(5, Node(6, Node(4)))

	summed = add_two_numbers(head_a, head_b)
	print_list(summed)  # 7 -> 0 -> 8
