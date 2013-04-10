from Node import pEdge 

#This is an abstract class, it should not be instantiated.
class ReflexionBuilder:
	#edgetype can take dotted, dashed, solid
	def __init__(self, nodes, verbose):
		self.currentNodes = nodes
		self.verbose = verbose

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
				if self.verbose: print nodeSrc.label + ' -> ' + nodeDest.label + ' changed from' + edge.type +'to solid';
				edge.type = 'solid'
				notfound = False
			elif edge.type == 'solid':
				notfound = False

		#else,  artifact call were not specified on the conceptual architecture
		#change line to divergence (dashed)
		if notfound:
			nodeSrc.addEdge(pEdge(nodeDest, 'dashed'))
			if self.verbose: print nodeSrc.label + ' -> ' + nodeDest.label + ' created line to dashed';
		return

	def getNodeForFilename(self, filename):
		for key, node in self.currentNodes.items():
			for regex in node.listValidRegex:
				if(regex.search(filename.strip())):
					if self.verbose: print "Match! : " + filename + " -> " + key
					return node
		if self.verbose: print "NO Match! : " + filename		
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



