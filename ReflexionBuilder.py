from Node import pEdge 
class ReflexionBuilder:
	#edgetype can take dotted, dashed, solid
	def __init__(self, nodes):
		self.currentNodes = nodes

	def getCallerOrigin(self, line):
		raise NotImplementedError( "Should have implemented this on child class" )

	def getCallingDestination(self, line):
		raise NotImplementedError( "Should have implemented this on child class" )

	"""
	absence (dotted), call that we expected to have but was not found in the artifacts.

	divergence (dashed), artifact call that were not specified on the conceptual architecture

	convergence (solid), match correctly
	"""
	def createEdge(self, nodeSrc, nodeDest):
		#found a nodeDest in the NodeSrc Edge list
		#change line to convergence, match correctly (solid)
		notfound = True
		if nodeSrc.myEdges.has_key(nodeDest.label):
			edge = nodeSrc.myEdges[nodeDest.label]
			if edge.type == 'dotted':
				edge.type = 'solid'
				notfound = False

		#else,  artifact call were not specified on the conceptual architecture
		#change line to divergence (dashed)
		if notfound:
			nodeSrc.addEdge(pEdge(nodeDest, 'dashed'))
		return

	def getNodeForFilename(self, filename):
		for key, node in self.currentNodes.items():
			for regex in node.listValidRegex:
				if(regex.search(filename.strip())):
					print "Match! : " + filename + " -> " + key
					return node
		print "NO Match! : " + filename		
		return None

	def buildReflexion(self,filename):
		try:
			f = open(filename, 'r')
			for line in f.readlines():
				srcNode = self.getNodeForFilename(self.getCallerOrigin(line))
				destNode = self.getNodeForFilename(self.getCallingDestination(line))
				if(srcNode and destNode):
					self.createEdge(srcNode, destNode)

		except IOError:
			print 'cannot open', filename
			return None



