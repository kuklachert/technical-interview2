# Data Science Nanodegree – Career Development
## Technical Interview Practice – Explanations
### ILLYA PAYANOV

**Question 1**

Assumptions/definitions:

*	To fulfil the criteria of an anagram, String 1 and String 2 must contain the same set of characters, i. e.: 1) no character can only occur in one of the strings and 2) each character exists in both strings in the same quantity.

Approach:
*	Loop through every substring of s that has the same length as t and check if the substring and t are anagrams.
*	To check if two strings of the same length are anagrams of each other, do the following:
  -	Loop through every character of the first string.
  -	Check if the character exists in the second string and remove it from the second string if it does. The removal ensures that the quantity of the characters in each string is accounted for.
  -	If a character in the first string cannot be found in the second string, two strings are not anagrams and the check can be interrupted.
  -	If all characters of the first string are looped through and found in the second string, the two strings are anagrams of each other.

Test cases:
*	Boundary case: None is any or both of the inputs (must return False).
*	Boundary case: t is longer than s (must return False).
*	s contains all symbols of t but no substring of t is an anagram of s (see code, must return False).
*	there is an anagram of t in at least one substring of s (see code, must return True).

Efficiency (worst case):
*	The outer loop (main function) is repeated len(s) times.
* The 1st inner loop (helper function checkAnagram) is repeated len(t) times.
*	The 2nd inner loop (helper function checkAnagram) is repeated len(t) times.
*	The worst case efficiency must therefore be **O (n^3)**.
*	In the helper function removeCharFromString, an index method is used, which may also worsen the efficiency of the main function depending on the implementation of the method in Python.

Space complexity:
* Apart from the input variables, the following additional space is used:
  - An integer counter variable is used in the for loop.
  - An additional string variable with the same length as t is passed over to the helper function q1_checkAnagram.
  - In the helper function q1_removeCharFromString, an integer variable is used to store the index of the char to be removed.
* The overall space complexity must therefore be **O (n)**.

**Question 2**

Assumptions/definitions:

*	A palindromic string is a string that reads the same forwards and backwards.
*	There are two types of palindromic strings that have to be handled slightly differently by the code:
  -	Type 1: palindromic string without a middle character (e.g. ABBA)
  -	Type 2: palindromic string with a middle character (e.g. ASA)
*	While checking for “palindromity”, spaces are not ignored and upper/lower case characters are not treated as the same for the sake of simplicity (this is at least how I understood “palindromic string” as opposed to “palindrome”).
*	In case no palindromic strings are found in the string, the first character of the string is returned (a one-character string is technically a palindromic string). 

Approach:
*	Loop through every character of the input string as the potential starting character of a palindromic string.
* For each starting character, check every possible substring (by looping through all the characters to the right of the starting character) for a palindrome. To check for palindromes, do the following:
  - If a given substring has an even number of characters (Type 1), compare the left half to the inverse of the right half
  - If the number of characters is odd (Type 2), compare the substring to the left of the middle character with the inverse of the substring to the right.
* If a palindrome is found, compare it to the current longest palindrome and overwrite if the new palindrome is longer.

Test cases:
*	Boundary case: None as input (must return False).
*	Boundary case: string without palindromic substrings (see code, must return the first character).
*	String with multiple palindromic substrings, including a shorter palindromic string which is part of the left half of a longer palindromic string (see code, must return the longest palindromic string).

Efficiency (worst case):
*	In the first iteration of the outer loop, the inner loop is repeated a maximum of (len(a)-1) times.
* In the subsequent iterations, the inner loop is repeated a maximum of (len(a)-2) times.
*	The worst case efficiency must therefore be **O (n^2)**.

Space complexity:
* Apart from the input variables, the following additional space is used:
  - To store the current longest palindrome, a string variable is used. Its maximum length can equal the length of a.
  - Two integer counter variables are used in the for loops.
* The overall space complexity must therefore be **O (n)**.

**Question 3**

Approach:
*	Start with the lightest edge (i. e. the edge with the lowest weight) and add it to the (formerly empty) adjacency list. The presence in the adjacency list serves as a “connected” marker for both nodes connected by the lightest edge.
*	Loop through the remaining edges in the following order: second-lightest edge, third-lightest edge etc. (the edges must be sorted beforehand).
*	If an edge is found that adds a further node to the spanning tree (i.e. it connects a connected node to an unconnected one), add it to the adjacency list.
*	Repeat the loop (always starting from the second-lightest edge) (n-2) number of times, where n is the total number of nodes. 
Every iteration should connect a new node to the spanning tree, and with the first 2 nodes already added during the initial step, (n-2) steps must be enough to connect all the nodes.
*	Check if every node is represented in the spanning tree. If not every node is represented, there are parts of the graph disconnected from the starting point which means no spanning tree exists.

Test cases:
*	Boundary case: None as input (must return None)
*	Boundary case: empty graph (must return None)
*	Disconnected graph (see code, must return None)
*	Connected graph (see code, must return the shortest spanning tree).

Efficiency (worst case):
*	Let n be the number of edges in the graph and m be the number of nodes.
* The creation of the nodes list would take n iterations.
*	The creation of the edges list would take m iterations.
*	Assuming that Python’s sort function uses one of the quicker search algorithms (such as Merge Sort), it would take n*log(n) times to sort all the edges by their weight.
*	The outer loop is repeated (n-2) times.
*	The inner loop is repeated (n-1) times.
*	The final check (is every node represented in the adjacency list?) is done using m iterations.
*	The overall number of operations is therefore n+2m+n*log(n)+(n-1)(n-2).
*	I presume the worst case efficiency would in this case be **O(n^2)** corresponding to the least efficient section of the algorithm.
	
**Question 4**

Assumptions/definitions:

* As stated in the project description, I assume that T does indeed adhere to all BST rules and both n1 and n2 exist in T. This allows me to bypass multiple tedious plausibility checks that would be needed to be run without the assumption.

Approach:
* Use the root as the starting node
* If n1 and n2 are on the opposite sides of the starting node (i. e. one of the two is larger and the other one is smaller than the node), the starting node is the lowest common ancestor (LCA) due to properties of the BST.
* If n1 and n2 are on the same side of the starting node, move the starting node to the child of the previous starting node that is on the same side of the root as n1 and n2 and repeat the previous step.
* At some point, n1 and n2 would be split by the current starting node which would mean the current starting node is the LCA.

Test cases:
* Boundary case: T=None (must return None)
* Boundary case: r=None (must return None)
* n1 and n2 are directly related, i.e. one is a direct ancestor of the other (see code, must return the parent of the upper node)
* LCA is the root (see code, must return the root)
* LCA is a non-root node, n1 and n2 are on different levels of T, n1<n2 (see code, must return the LCA correctly)
* LCA is a non-root node, n1 and n2 are on the same level of T, n1>n2 (see code, must return the LCA correctly)

Efficiency (worst case): 
* Let n represent the number of nodes in the tree.
* To find children of the current starting node, n iterations must be made.
* To go down the tree and compare n1 and n2 to the current starting node, the maximum number of iterations is equal to the number of levels in the tree. In the worst case (every node in the tree has one child), this number is n.
* The overall efficiency must therefore be **O (n ^ 2)**.

**Question 5**

Approach:
* Identify the m-th next element from the head. The head and the m-th next element are the 1st and the 2nd cursor.
* Move both cursors one element to the right until the 2nd cursor finds the end ot the linked list.

Test cases:
* Boundary case: ll is None (must return None)
* Boundary case: m is larger than the length of ll (must return None)
* m = 1 (see code, must return the last element of ll)
* “Normal case”: 1 < m < length of ll (see code, must return the element that is the mth away from the end).

Efficiency (worst case):
* To find the m-th next element from the head, m steps are needed.
* The *while* loop moving both cursors to the right takes (length of ll - m) steps.
* This results in the worst case efficiency of **O (n)**.
