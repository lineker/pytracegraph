from Node import pEdge 
class ReflexionBuilder:
	#edgetype can take dotted, dashed, solid
	def __init__(self, nodes):
		self.currentNodes = nodes

	def parseLine(self, line):
		p1 = line.split()
		return [p1[1].split(':')[0],p1[3].split(':')[0]]

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
				lineParsed = self.parseLine(line)
				#print lineParsed
				srcNode = self.getNodeForFilename(lineParsed[0])
				destNode = self.getNodeForFilename(lineParsed[1])
				if(srcNode and destNode):
					self.createEdge(srcNode, destNode)

		except IOError:
			print 'cannot open', filename
			return None



