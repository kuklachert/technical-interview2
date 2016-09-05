"""
Main function for Question 1
"""

def question1 (s,t):

    # Treat a boundary case when one of the inputs is None

    if t==None or s==None:
        return False
    
    # If t is longer than s, there's no possibility of a substring of s
    # being an anagram of t

    if len(t)>len(s):
        return False

    # Go through substrings of s that have the same length as t 
    # and check for anagrams

    for i in range(0,len(s)):
        if (s[i] in t and len(s)-i>=len(t)):
            if q1_checkAnagram(s[i:i+len(t)],t):
                return True

    # Return False in case no anagram was found   

    return False

"""
Helper function to check if string1 is an anagram of string2
"""
def q1_checkAnagram (string1,string2):
    for char in string1:

        # Char removal is necessary to ensure that repeated chars are
        # accounted for in the comparison
        # Example: "ana" is not an anagram of "ann", but would be
        # treated as such without the removal of chars,
        # as every char of "ana" exists in "ann" and vice versa.

        if char in string2:
            string2=q1_removeCharFromString(string2,char)
        else:
            return False

    # if no False has been returned up to this point, it means that
    # every char in string1 is contained in string2 in exactly the same
    # quantity, which meets the definition of anagram.
    # Therefore return True    

    return True

"""
Helper function to remove a char from a string
"""

def q1_removeCharFromString (string,char):

    i=string.index(char)
    return string[:i]+string[i+1:]

"""
Test Cases for question1
"""

print "Test Cases Question 1:"

# must return False per definition
print question1 (None,None)

# must return False per definition
print question1 ("mam","mtzamr")

# must return False
print question1 ("mtzamr","mam")

# must return True as "amr" is an anagram of "ram"
print question1 ("mtzamr","ram")
print

"""
Main function for Question 2
"""

def question2(a):

    # Handle boundary cases

    if a==None or a=="":
        return None

    # In case no palindrome is found, the first character of the string
    # is treated as the longest palindrome
    
    longest_palindrome=a[0]

    # Go through potential starting points of the palindrome
    # This could be every char in the string except the last one

    for i in range(0,len(a)-1):

        # Check every possible substring starting with i-th character
        # for palindromes

        for j in range(i, len(a)):

            if checkForPalindrome(a[i:j]):
                if (j-i)>len(longest_palindrome):
                    longest_palindrome=a[i:j]

    return longest_palindrome

"""
Helper function to look for "true" palindromes
"""

def checkForPalindrome(string):

    # For strings with odd length, the middle character has to be
    # omitted from the comparison of the left and the right half

    if len(string)%2==1:
        if string[:(len(string)-1)/2]==string[len(string):len(string)/2:-1]:
            return True

    # Otherwise, compare the first n/2 characters with the last n/2
    # in inverted order

    else:
        if string[:len(string)/2]==string[len(string):len(string)/2-1:-1]:
            return True

    return False

"""
Test Cases for question1
"""

print "Test Cases Question 2:"

# Must return None per definition
print question2(None)

# Must return "a" per definition
print question2("abcdefghijklma")

# Must return "qamaddamaq"
print question2("hdfqamaddamaqzbhf")
print

"""
Main function for Question 3
"""

def question3(G):

    # Handle boundary cases
    if (G==None) or (G=={}):
        return None

    # Create lists of nodes and edges

    nodes=[]
    edges=[]

    for node in G:
        nodes.append(node)
        for edge in G[node]:
            if ([edge[1],edge[0],node] not in edges):
                edges.append([edge[1], node, edge[0]])

    edges=sorted(edges,key = lambda edges: edges[0])

    # Start with the lightest edge

    adj_list={}
    adj_list[edges[0][1]]=[(edges[0][2],edges[0][0])]
    adj_list[edges[0][2]]=[(edges[0][1],edges[0][0])]

    # Loop through the sorted edges list (n-2) times
    # Each iteration should add exactly 1 new edge to the adjacency
    # list, so not more than (n-2) interations are required

    for i in range(0,len(nodes)-2):

        # Start with the second lightest edge
        # Each time an edge that connects a node not in adj_list to a
        # node that already is there, update adj_list and end the loop
        
        for edge in edges[1:]:
            if (edge[1] in adj_list) and (edge[2] not in adj_list):
                adj_list[edge[1]].append((edge[2],edge[0]))
                adj_list[edge[2]]=[(edge[1],edge[0])]
                break
            if (edge[2] in adj_list) and (edge[1] not in adj_list):
                adj_list[edge[2]].append((edge[1],edge[0]))
                adj_list[edge[1]]=[(edge[2],edge[0])]
                break

    # Check if every node is represented in adj_list
    # If not, we are dealing with a disconnected graph which has
    # no spanning trees

    for node in nodes:
        if node not in adj_list:
            return None

    return adj_list


"""
Test cases for Question 3
"""

print "Test Cases Question 3:"

# Must return None
print question3(None)

# Must return None
g1={}
print question3(g1)

# Disconnected graph - must return None

g2={'A':[('B',3),('C',4)],
    'B':[('A',3),('C',2)],
    'C':[('A',4),('B',2)],
    'D':[('E',5)],
    'E':[('D',5)]}
print question3(g2)

# Connected graph - must return an adjacency list corresponding to A-B-C-D-E
g3={'A':[('B',3),('D',4)],
    'B':[('A',3),('C',2),('E',7)],
    'C':[('B',2),('D',2)],
    'D':[('A',4),('C',2),('E',5)],
    'E':[('B',7),('D',5)]}
print question3(g3)
print

"""
Main function for Question 4
"""
def question4(T,r,n1,n2):

    # Handle boundary cases

    if T==None or r==None:
        return None

    # Define the current LCA (least common ancestor) as the root

    lca=r

    # reorder n1 and n2 such that n1<n2:

    n1,n2=n2,n1

    # If n1 and n2 are on the opposite side of the current LCA,
    # the final LCA is the current LCA

    if (n1<lca) and (n2>lca):
        return lca
    
    # Otherwise, look for children of the current LCA in the matrix

    children_of_lca=[None,None]

    for i in range(len(T[lca])):
        if (T[lca][i]==1) and (i<lca):
            children_of_lca[0]=i
        elif (T[lca][i]==1) and (i>lca):
            children_of_lca[1]=i

    # Handling the boundary case where n1 is a direct ancestor if n2
    # or vice versa

    if (n1 in children_of_lca) or (n2 in children_of_lca):
        return lca

    # If both n1 and n2 are on the right side of the current LCA,
    # search for final LCA recursively in the right side of the
    # current branch

    if (n1>lca) and (n2>lca):
        lca=children_of_lca[1]
        return question4(T,lca,n1,n2)

    # If both n1 and n2 are on the left side of the current LCA,
    # search for final LCA recursively in the left side of the
    # current branch

    elif (n1<lca) and (n2<lca):
        lca=children_of_lca[0]
        return question4(T,lca,n1,n2)

"""
Test cases for Question 4
"""

print "Test Cases Question 4:"
# Must return None
print question4 (None, 3, 1, 4)

# Must return None
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]], None, 1, 4)


# Must return 1
# 2 is the parent of 3, so the LCA must be the parent of 2
print question4([[0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1],
                 [0, 0, 0, 0]], 0, 2, 3)

# Example from the project description
# Must return 3
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],3,1,4)

# Must return 3
# 4 is the uncle/aunt of 0
# 3 is the grandparent of 0 and the parent of 4
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]],5,0,4)
# Must return 1
# Both 2 and 0 are children of 1
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]],5,2,0)
print

"""
Define classes for Question 5
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
           
"""
Main function for Question 5
"""

def question5(ll,m):

    # Handle boundary cases

    if ll==None or m==None:
        return None

    if  m<1:
        return None

    # Start searching from the head of the linked list

    current=ll.head

    # Identify the m-th next element from the head

    j=0
    mth_next=current

    while j<m:

        if mth_next==None and j<m:
            return None
        mth_next=mth_next.next
        j+=1
    
    # Move both current and mth_next one step to the right
    # until mth_next finds the end of the linked list

    while mth_next:

        current=current.next
        mth_next=mth_next.next

    return current.value

"""
Test cases for Question 5
"""

print "Test Cases Question 5:"
# Must return None
print question5 (None,2)

# Create a linked list for testing
e1 = Element(5)
e2 = Element(10)
e3 = Element(15)
e4 = Element(20)
e5 = Element(25)
ll=LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)

# Must return None
print question5(ll,6)
# Must return 25 (last element)
print question5(ll,1)
# Must return 20
print question5(ll,2)

print
