from py2neo import Graph, Node, Relationship, RelationshipMatcher, NodeMatcher, RelationshipMatch, NodeMatch

uri='bolt://localhost:7687'

class Neo:
   def __init__(self):
      super().__init__()
      self.graph=Graph(host='localhost', user='neo4j', password='password')
   # return Cursor
   def exeCql(self, cql):
      return self.graph.run(cql)
   
def testNodeMatcher():
   graph=Graph(host='localhost', user='neo4j', password='password')
   matcher=NodeMatcher(graph)
   results=matcher.match('Person')# type NodeMatch. unknown error if add properties
   # print(result)
   for result in results:
      print(result) # type Node
   olders=results.where('_.age=20')
   for older in olders:
      print(older)

def testNodeMatch():
   graph=Graph(host='localhost', user='neo4j', password='password')
   match=NodeMatch(graph)
   results=match.where("_.name=~'.*j' and _.age>21")
   for result in results:
      print(result)

def testRelationshipMatch():
   graph=Graph(host='localhost', user='neo4j', password='password')
   match=RelationshipMatch(graph)
   results=match.where("_.status='now'")
   print(results)
   for i in results:
      print(type(i))

def testRelationshipMatcher():
   graph=Graph(host='localhost', user='neo4j', password='password')
   matcher=RelationshipMatcher(graph)
   results=matcher.match(None, 'LiveIn') # type RelationshipMatch
   for result in results:
      print(type(result))

if __name__=='__main__':
   graph=Graph(host='localhost', user='neo4j', password='password')
   # create node
#    node=Node('Process', name='log')
#    graph.create(node)
   #testNodeMatcher()
   #testNodeMatch()
   testRelationshipMatch()
   #testRelationshipMatcher()