import pydot
import argparse
from Node import pNode, pEdge 

#from MyParser import simpleParser
#from MyReflexionBuilder import simpleReflexionBuilder

def my_import(filename, classname):
	mod = __import__(filename, fromlist=[classname])
	klass = getattr(mod, classname)
	return klass

parser = argparse.ArgumentParser(description='Generate graphs & reflexion models from any trace files')
parser.add_argument('-n','--nodes', help='File contain nodes data', required=True)
parser.add_argument('-e','--edges', help='File contain edges data', required=True)
parser.add_argument('-p','--parser', help='Parser filename and class [ie. MyParser.simpleParser]', required=True)
parser.add_argument('-r','--reflexion', help='File with data to build reflexion model', required=False)
parser.add_argument('-rp','--reflexionparser', help='Reflexion parser filename and class [ie. MyReflexionBuilder.simpleReflexionBuilder]', required=False)
parser.add_argument('-w','--write', help='output file', required=True)
parser.add_argument('-v','--verbose', help='print debug text', required=False, action='store_true')
args = vars(parser.parse_args())

def buildReflexion(mnodes):
	if not args['reflexionparser']:
		print '--reflexion can only be set when a --reflexionparser is set'
		return
	r = args['reflexionparser'].split('.')
	#dynamic load of parser class
	sr = my_import(r[0],r[1])
	refBuilder = sr(mnodes,args['verbose']) #simpleReflexionBuilder(mnodes)
	refBuilder.buildReflexion(args['reflexion'])

if args['nodes'] and args['edges']:
	p = args['parser'].split('.')
	#dynamic load of parser class
	sp = my_import(p[0],p[1])
	parser = sp(args['verbose']) #simpleParser()
	print '==== BUILDING CONCEPTUAL MODEL ===='
	mnodes = parser.parse(args['nodes'], args['edges'])

	if args['reflexion']:
		print '==== BUILDING REFLEXION MODEL ===='
		buildReflexion(mnodes)

	graph = pydot.Dot(graph_type='digraph')
	for item in mnodes.values():
		graph.add_node(item.getPydotObj())
		for edge in item.myEdges.values():
			graph.add_edge(edge.getPydotObj(item))

	graph.write_png(args['write']) #example2.png
	print "Done"