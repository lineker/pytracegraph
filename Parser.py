from Node import pNode, pEdge 

#This is an abstract class, it should not be instantiated.
class Parser( object ):
    """This is an abstract class for a Parse"""
    def __init__(self,verbose):
    	self.parsedNodes = {}
        self.verbose = verbose

    def openFile(self, filename):
        try:
        	f = open(filename, 'r')
        	return f
    	except IOError:
        	print 'cannot open', filename
        	return None


    #return Node object
    def parseNodeLine( self, strline ):
        raise NotImplementedError( "Should have implemented this" )

    #return list with [origin label, destination label] representing a Edge
    def parseEdgeLine( self, strline ):
        raise NotImplementedError( "Should have implemented this" )

    def parseNodesFromFile( self, filename ):
        if self.verbose: print 'parsing nodes from : %s' %(filename) 
        #For each line of file
        f = self.openFile(filename)
        if f is not None:
        	for line in f.readlines():
        		node = self.parseNodeLine(line)
		        #if node is not None
        		if(node):
        			if(node.label in self.parsedNodes):
        				#node already exist so just update regex list
        				self.parsedNodes[node.label].listValidRegex.append(node.listValidRegex[0])
        			else:
    				    #add Node to parsedNodes
        				self.parsedNodes[node.label] = node

    def parseEdgesFromFile( self, filename ):
    	if self.verbose: print 'parsing edges from : %s' %(filename) 
        f = self.openFile(filename)
        if f is not None:
        	#For each line of file
        	for line in f.readlines():
        		#parseEdgeLine()
        		currentEdge = self.parseEdgeLine(line)
        		#print currentEdge
        		#if list is not empty
        		if(currentEdge and len(currentEdge) >= 2):

        			#Find Destinantion Node that match label
        			if(currentEdge[0] in self.parsedNodes and currentEdge[1] in self.parsedNodes):
        				#Add Edge and Type to origin Node if destination and origin node
        				#were found in parsedNodes
        				self.parsedNodes[currentEdge[0]].addEdge(pEdge(self.parsedNodes[currentEdge[1]]))
        			else:
        				if self.verbose: print "Found an Edge for Nodes that do not exist, ignoring..."

    def parse( self, NodesFilename, edgesFilename = "" ):
        if(NodesFilename is None):
        	raise Exception('Filename not provide')
        #parse Nodes
        self.parseNodesFromFile(NodesFilename)
        if edgesFilename:
        	self.parseEdgesFromFile(edgesFilename)
        else:
        	self.parseEdgesFromFile(NodesFilename)

        return self.parsedNodes
