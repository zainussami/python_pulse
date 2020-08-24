class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

    #Print the List
    def printList(self):
        node = self
        output= ''
        while node != None:
            output += str(node.val)
            output += "->"
            node = node.next
        print(output)

    def reverseIteratively(self,head):
        currentNode = head
        previousNode = None
        nextNode = None

        while currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode

            previousNode = currentNode
            currentNode = nextNode
        return previousNode


testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()

testHead.reverseIteratively(testHead)
#testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
    

