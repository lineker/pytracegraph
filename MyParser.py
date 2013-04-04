from Parser import Parser 
from Node import pNode, pEdge 
class simpleParser( Parser ):

	#return Node object
	def parseNodeLine( self, strline ):
        #select file regex
        #select mapTo label
        #create Node
        #return Node
		s = strline.strip().split()
		print s
		if len(s) == 2:
			node = pNode(s[0])
			node.addValidRegex(s[1])

		return node

	#return list with [origin label, destination label] representing a Edge	
	def parseEdgeLine( self, strline ):
		return strline.split()