from simplexclient.objectclient import SimplexClass

import random

class Activity(SimplexClass):
  connection='default'
  classTitle='Activity'

  def createContainer(self):
    newContainer=ChildrenContainer(ndx=str(random.random()))
    newContainer.save()
    self.link('parent2container',newContainer)
    return newContainer

class Port(SimplexClass):
  connection='default'
  classTitle='Port'

class ChildrenContainer(SimplexClass):
  connection='default'
  classTitle='ChildrenContainer'

class ChildBinding(SimplexClass):
  connection='default'
  classTitle='ChildBinding'


for cls in [Activity,Port,ChildrenContainer,ChildBinding]:
  cls.register()
