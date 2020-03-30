from py2neo import Graph, Node, Relationship



if __name__=='__main__':
   graph=Graph(host='localhost', user='neo4j', password='password')
   # create node
#    node=Node('Process', name='log')
#    graph.create(node)