#Alannah Steck
#U6L6
#Binary Search Tree
#૮꒰ ˶• ༝ •˶꒱ა  Good Luck Bunny is here

class BinarySearchTree:
  class BinaryNode:
    def __init__(self, value):
      self.__value = value
      self.__parent = None
      self.__left = None
      self.__right = None

    def __lt__(self,other):
      if type(other) == type(self):
        return self.__value < other.__value
      else:
        raise Exception("both objects must be nodes")

    def __gt__(self,other):
      if type(other) == type(self):
        return self.__value > other.__value
      else:
        raise Exception("both objects must be nodes")

    def __eq__(self,other):
      '''determine if positions are equal'''
      if type(other) == type(self):
        return self.__value == other.__value
      else:
        raise Exception("both objects must be nodes")

    def __str__(self):
      return f"|{self.__value}|"

  def __init__(self):
    self.__root = None
    self.__size = 0

  def inorder_traversal(self, pointer=None):
    '''gets values by moving left, storing, then moving right'''
    if pointer is None:
      if self.__size == 0:
        return []
      pointer = self.__root
    if pointer._BinaryNode__left is None and pointer._BinaryNode__right is None:
      num = 0
    elif pointer._BinaryNode__left is not None and pointer._BinaryNode__right is not None:
      num = 2
    else:
      num = 1
    valList = []
    if num != 0:
      if pointer._BinaryNode__left is not None: 
        leftList = self.inorder_traversal(pointer._BinaryNode__left)
        for item in leftList:
           valList.append(item)
      valList.append(pointer._BinaryNode__value)
      if pointer._BinaryNode__right is not None:
        rightList = self.inorder_traversal(pointer._BinaryNode__right)
        for item in rightList:
           valList.append(item)
    else:
      valList.append(pointer._BinaryNode__value)
    return valList

  def __str__(self):
    '''prints the list'''
    return str(self.inorder_traversal())

  def insert(self,goingToAdd,currentNode=None):
    '''inserts a new value into the tree as a leaf'''
    if type(goingToAdd) != int:
      raise Exception("Can only add integers")
    if currentNode is None:
      if self.__root is None:
        newRoot = self.BinaryNode(goingToAdd)
        self.__root = newRoot
        self.__size += 1
        return
      currentNode = self.__root
    if goingToAdd == currentNode._BinaryNode__value:
      raise Exception("Can't insert duplicate values")
    elif goingToAdd > currentNode._BinaryNode__value:
      nextNode = currentNode._BinaryNode__right
    else:
      nextNode = currentNode._BinaryNode__left
    if nextNode is not None:
      self.insert(goingToAdd,nextNode)
    else: 
      if goingToAdd > currentNode._BinaryNode__value:
        newNode = self.BinaryNode(goingToAdd)
        currentNode._BinaryNode__right=newNode
        newNode._BinaryNode__parent=currentNode
        self.__size += 1
      else:
        newNode = self.BinaryNode(goingToAdd)
        currentNode._BinaryNode__left=newNode
        newNode._BinaryNode__parent=currentNode
        self.__size += 1
      
  def get_min(self, optionalRoot=None):
    '''gets the smallest node'''
    if self.__root is not None:
      if optionalRoot is None:
        currentNode = self.__root
      else:
        currentNode = optionalRoot
      while currentNode._BinaryNode__left is not None:
        currentNode = currentNode._BinaryNode__left
      valList = self.inorder_traversal()
      return currentNode
    else:
      raise Exception("cant get max of an empty tree")

  def get_max(self,optionalRoot=None):
    '''gets the biggest node'''
    if self.__root is not None:
      if optionalRoot is None:
        currentNode = self.__root
      else:
        currentNode = optionalRoot
      while currentNode._BinaryNode__right is not None:
        currentNode = currentNode._BinaryNode__right
      valList = self.inorder_traversal()
      return currentNode
    else:
      raise Exception("cant get max of an empty tree")

  def __len__(self):
    """returns the length of the list"""
    return self.__size

  def delete(self,deleteThis,currentNode=None):
    '''Deletes a node from the tree'''
    if self.__size == 0: #checks if list is empty
      raise Exception("Cannot delte from an empty list")
    if currentNode is None: #finding the node 
      currentNode = self.__root
    if deleteThis is not currentNode._BinaryNode__value:
      if deleteThis > currentNode._BinaryNode__value:
        if currentNode._BinaryNode__right is None:
          raise Exception("Cannot delete a node that doesn't exist")
        self.delete(deleteThis,currentNode._BinaryNode__right)
      else:
        if currentNode._BinaryNode__left is None:
          raise Exception("Cannot delete a node that doesn't exist")
        self.delete(deleteThis,currentNode._BinaryNode__left)
    else: 
      if currentNode._BinaryNode__left is None and currentNode._BinaryNode__right is None: #0 child
        if self.__root is currentNode:
          self.__root = None
        deletedParent = currentNode._BinaryNode__parent
        if deletedParent._BinaryNode__left is currentNode:
          deletedParent._BinaryNode__left = None
        else:
          deletedParent._BinaryNode__right = None
        self.__size -= 1
      elif currentNode._BinaryNode__left is not None and currentNode._BinaryNode__right is not None: #2 child
        minNode = self.get_min(currentNode._BinaryNode__right)
        self.delete(minNode._BinaryNode__value)
        currentNode._BinaryNode__value = minNode._BinaryNode__value
      else: #1 child
        if currentNode._BinaryNode__left is not None:
          deletedChild = currentNode._BinaryNode__left
        else:
          deletedChild = currentNode._BinaryNode__right
        if self.__root is currentNode:
          self.__root = deletedChild
          deletedChild._BinaryNode__parent = None
          return
        deletedParent = currentNode._BinaryNode__parent
        if deletedChild < deletedParent:
          deletedChild._BinaryNode__parent = deletedParent
          deletedParent._BinaryNode__left = deletedChild
        else:
          deletedChild._BinaryNode__parent = deletedParent
          deletedParent._BinaryNode__right = deletedChild
        self.__size -= 1



