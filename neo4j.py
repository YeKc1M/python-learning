from py2neo import Graph, Node, Relationship, RelationshipMatcher, NodeMatcher, RelationshipMatch, NodeMatch
import py2neo.ogm

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
      print(result['name']) # type Node
   olders=results.where('_.age=20')
   for older in olders:
      print(older['name']+str(older['age']))

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
      print(type(i))# type Relation
      print(i['status'])

def testRelationshipMatcher():
   graph=Graph(host='localhost', user='neo4j', password='password')
   matcher=RelationshipMatcher(graph)
   results=matcher.match(None, 'LiveIn') # type RelationshipMatch
   for result in results:
      print(type(result))# type Relation
      print(result['status'])

def test():
   graph=Graph(host='localhost', user='neo4j', password='password')
   matcher=NodeMatcher(graph)
   results=matcher.match('Person')
   l=list(results)
   print(l[0]['name'])

def tfidf():
   graph=Graph(host='localhost', user='neo4j', password='password')
   rs=graph.run('match(n) return id(n) as id, n.name as name').data()
   with open('tfidf.txt','w', encoding='utf-8') as f:
      for r in rs:
         f.write(r['name']+'\n')

if __name__=='__main__':
   graph=Graph(host='localhost', user='neo4j', password='password')
   # create node
#    node=Node('Process', name='log')
#    graph.create(node)
   #testNodeMatcher()
   #testNodeMatch()
   #testRelationshipMatch()
   #testRelationshipMatcher()
   #test()
   tfidf()