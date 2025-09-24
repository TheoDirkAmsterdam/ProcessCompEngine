from simplexclient.objectclient import SimplexClass

import random

class Job(SimplexClass):
  connection='default'
  classTitle='Activity'

  def createRelationshipBindingContainer(self):
    newContainer=RelationshipBindingContainer(ndx=str(random.random()))
    newContainer.save()
    self.link('job2relationshipcontainer',newContainer)
    return newContainer

class Port(SimplexClass):
  connection='default'
  classTitle='Port'

class RelationshipBindingContainer(SimplexClass):
  connection='default'
  classTitle='RelationshipBindingContainer'

class RelationshipBinding(SimplexClass):
  connection='default'
  classTitle='RelationshipBinding'

class InputPort(SimplexClass):
  connection='default'
  classTitle='InputPort'

class OutputPort(SimplexClass):
  connection='default'
  classTitle='OutputPort'

class PortCoupling(SimplexClass):
  connection='default'
  classTitle='PortCoupling'

class SequenceController(SimplexClass):
  connection='default'
  classTitle='SequenceController'




for cls in [Activity,Port,ChildrenContainer,ChildBinding]:
  cls.register()
