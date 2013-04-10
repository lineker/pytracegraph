import pydot
import re
class pEdge:
	#edgetype can take dotted, dashed, solid
	def __init__(self, node, edgetype = 'dotted'):
		self.type = edgetype
		self.destNode = node
		self.callcounts = 1
		self.pydotObject = None

	def getPydotObj(self, origin):
		if not self.pydotObject:
			self.pydotObject = pydot.Edge(origin.getPydotObj(), self.destNode.getPydotObj(), style=self.type) 
		return self.pydotObject

	def increaseCallCounts(self):
		self.callcounts = self.callcounts + 1

	def __str__(self):
		return "[edgetype:%s to:%s>" % (self.type, self.destNode.label)

class pNode:
	def __init__(self,label):
		self.label = label
		#list of regex strings
		self.listValidRegex = []
		#dictionary of key=Node.label, value=Edge object
		self.myEdges = {} 

	def getPydotObj(self):
		return pydot.Node(self.label, shape="rect")

	def addEdge(self,edge):
		#print self.label + ' -> ' + edge.destNode.label + ' : ' + edge.type
		self.myEdges[edge.destNode.label] = edge

	def addValidRegex(self,regex):
		self.listValidRegex.append(re.compile(regex, re.IGNORECASE))

	def __str__(self):
		return "<Node label:%s Edges:%s>" % (self.label, str(self.myEdges))
		#return "Node"


#m = p.match( 'string goes here' )
#if m:
#    print 'Match found: ', m.group()
#else:
#    print 'No match'