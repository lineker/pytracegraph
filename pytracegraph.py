import pydot
from Node import pNode, pEdge 
from MyParser import simpleParser
from MyReflexionBuilder import simpleReflexionBuilder

"""node = pNode('ThreadManager')
node2 = pNode('SessionManager')
myNodes = {}
myNodes['ThreadManager'] = node
print(myNodes['ThreadManager'])
node.addEdge(pEdge(node2))h
print(myNodes['ThreadManager'])
print(myNodes)"""

parser = simpleParser()
mnodes = parser.parse('nodes.txt', 'edges.txt')
#print(mnodes['ThreadManager'].myEdges.itervalues().next())

refBuilder = simpleReflexionBuilder(mnodes)
refBuilder.buildReflexion('call_trace.txt')

graph = pydot.Dot(graph_type='digraph')
for item in mnodes.values():
	graph.add_node(item.getPydotObj())
	for edge in item.myEdges.values():
		graph.add_edge(edge.getPydotObj(item))

graph.write_png('example2.png')

string = "/msf/core/module"
for regex in mnodes['PenetrationModuleManager'].listValidRegex:
	if(regex.search(string)):
		print "Match!"
	else:
		print "No match!"