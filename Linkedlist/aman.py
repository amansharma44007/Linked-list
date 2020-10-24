class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
class LinkedList:
  def __init__(self):
    self.head=None
  def append(self,value):
    if self.head is None:
      self.head=Node(value)
      return
    nodeNext=self.head
    while nodeNext.next:
      nodeNext=nodeNext.next
    nodeNext.next=Node(value)
  def prepend(self,value):
    if self.head is None:
      self.head=Node(value)
      return
    nodeHead=Node(value)
    nodeHead.next=self.head
    self.head=nodeHead
  def insert(self,value,pos):
    if pos==0:
      self.prepend(value)
      return
    index=0
    node=self.head
    while node.next and index<=pos:
      if(pos-1)==index:
        new_node=Node(value)
        new_node.next=node.next
        node.next=new_node
        return
      index+=1
      node=node.next
    else:
      self.append(value)
      return 
  def printall(self):
    temp=self.head
    while temp:
      print(temp.value,end="->")
      temp=temp.next
    print("Null")
  def search(self,value):
    node=self.head
    flag=True
    while node:
      if value==node.value:
        print("Found")
        flag=False
      node=node.next
    if flag==True:
      print("Not here")
  def remove(self,value):
    if self.head is None:
      return
    if self.head.value==value:
      self.head=self.head.next
      return
    node=self.head
    flag=True
    while node.next:
      if node.next.value==value:
        node.next=node.next.next
        flag=False
        return
      node=node.next
    if flag==True:
      print("None present")
    
aman=LinkedList()
aman.append(22)
aman.append(33)
aman.prepend(44)
aman.printall()
aman.insert(11,0)
aman.insert(444,3)
aman.printall()
aman.search(99)
aman.remove(444)
aman.printall()
aman.remove(55)
