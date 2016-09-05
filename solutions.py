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

    # Remove from the beginning of the string    

    if i==0:
        return string[1:]

    # Remove from the end of the string   

    elif i==len(string)-1:
        return string[:i]

    # Remove from the middle of the string    

    else:
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

        palindrome=""
        left_half=""
        j=i

        # Check possible strings starting with i-th character for
        # palindromes

        while j < float(i+1)+float((len(a)-i)*0.5):

            # As long as there are no recurring characters in the string,
            # extend the left half of the eventual palindrome.
            # Do this as long as the maximum possible size of the left half
            # (roughly half of the substring starting with the i-th element)
            # is reached
            
            if a[j] not in left_half:
                left_half=left_half+a[j]
                j=j+1

            # As soon as one recurring character is found, check for "true"
            # palindromes containing left_half in the substring starting
            # with the i-th element
            # If a palindrome is found and is longer than the current
            # longest palindrome, overwrite longest_palindrome.

            else:
                palindrome=checkForPalindrome(a[i:], left_half)
                if len(palindrome)>len(longest_palindrome):
                    longest_palindrome=palindrome
                break

    return longest_palindrome

"""
Helper function to look for "true" palindromes
"""

def checkForPalindrome(string, left_half):

    right_half=""
    palindrome=""

    # Check for Type 1 palindromes (without a middle character, e.g. ABBA)
    
    if len(left_half)*2<=len(string):
        for i in range(len(left_half)*2-1,len(left_half)-1,-1):
            right_half=right_half+string[i]
        if right_half==left_half:
            palindrome=left_half+string[len(left_half):len(left_half)*2]

    # Check for Type 2 palindromes (with a middle character, e.g. ASA)

    # As Type 1 and Type 2 palindromes in the same substring containing the
    # same left half are mutually exclusive, there is no danger of
    # overwriting palindromes already found

    right_half=""
     
    for i in range(((len(left_half)-1)*2),len(left_half)-1,-1):
        right_half=right_half+string[i]
    if right_half==left_half[:-1]:
        palindrome=left_half+string[len(left_half):len(left_half)*2-1]

    # Recursively check for eventual longer palindromes of both types
    # Otherwise, longer palindromes containing short palindromes in the
    # left half (e.g. ABBANABBA) would be ignored

    left_half=left_half+string[len(left_half):len(left_half)+1]
    eventual_longer_palindrome=""

    # In the recursive checks, the left half of the eventual longer
    # palindrome is extended as long as the rest of the string
    # is large enough to provide an equally sized right half

    while len(left_half)*2<=len(string)+1:
        eventual_longer_palindrome=checkForPalindrome(string, left_half)
        left_half=left_half+string[len(left_half):len(left_half)+1]

        # Overwrite palindrome with the new palindrome found in the
        # recursion in case the new palindrome is longer
        # (new palindrome could also be "")
        
        if len(eventual_longer_palindrome)>len(palindrome):
            palindrome=eventual_longer_palindrome
           
    return palindrome

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
Define classes for Question 3
"""

class Edge(object):
    def __init__(self, value, node1, node2):
        self.value = value
        self.node1 = node1
        self.node2 = node2

class Graph(object):
    def __init__(self, edges=[]):
        self.edges = edges

"""
Main function for Question 3
"""

def question3(G):

    # Handle boundary cases
    if (G==None) or (G.edges==[]):
        return None

    # Create a list of nodes

    nodes=[]
    for edge in G.edges:
        if edge.node1 not in nodes:
            nodes.append (edge.node1)
        if edge.node2 not in nodes:
            nodes.append (edge.node2)

    # Create list of edges sorted by weight

    edges=[]
    for edge in G.edges:
        edges.append([edge.value,edge.node1,edge.node2])
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
g1=Graph()
print question3(g1)

# Disconnected graph - must return None
edge1=Edge(3,'A','B')
edge2=Edge(4,'A','C')
edge3=Edge(2,'B','C')
edge4=Edge(5,'E','D')
g2=Graph([edge1,edge2,edge3,edge4])
print question3(g2)

# Connected graph - must return an adjacency list corresponding to A-B-C-D-E
edge1=Edge(3,'A','B')
edge2=Edge(4,'A','D')
edge3=Edge(2,'B','C')
edge4=Edge(7,'B','E')
edge5=Edge(2,'C','D')
edge6=Edge(5,'D','E')
g3 = Graph ([edge1,edge2,edge3,edge4,edge5,edge6])
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

    if n1>n2:
        n3=n1
        n1=n2
        n2=n3

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

    # Start searching from the head of the linked list

    current=ll.head
    while current:

        # Look for the m-th next element from current
        # Stop searching if the end of ll is reached
        
        following=current.next
        j=1

        while j<m:

            following=following.next
            j+=1          
            if following==None:
                break

        # If the end is reached before the m-th next element is found,
        # length of ll is smaller than m. In this case return None

        if j<m:
            return None

        # Otherwise check if the end of the list is reached after
        # exactly m steps from current. If yes, return current.
        
        elif following==None:
            return current.value

        # Otherwise, repeat for the next element of the list.

        else:
            current=current.next

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
