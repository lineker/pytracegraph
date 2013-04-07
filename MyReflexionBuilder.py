from Node import pEdge 
from ReflexionBuilder import ReflexionBuilder

#Concrete implementation of class ReflexionBuilder
class simpleReflexionBuilder( ReflexionBuilder ):

	def getCallerOrigin(self, line):
		p1 = line.split()
		return p1[1].split(':')[0]

	def getCallingDestination(self, line):
		p1 = line.split()
		return p1[3].split(':')[0]