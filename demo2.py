import simplexclient.objectclient as oc
import json

import engine

# load server configurations
serverConf = json.load( open('./serverConf.json') ) #to be set
baseUrl = serverConf["baseUrl"]
usrpwd = serverConf["usrpwd"]

# create a client for accessing the S4D object store
client=oc.ObjectClient(baseUrl, usrpwd["user"], usrpwd["password"])

client.register('default')


# Search for a link class
# Activity -> ChildenContainer
Parent2Container=engine.Activity.links(title="parent2container")[0]

# Other side of the link class: ChildrenContainer
ChildrenContainer=Parent2Container.right
# this is the same as engine.ChildrenContainer


# Create a new treatment as a Python object
treatment=engine.Activity(title="Example Treatment",type="template")

# Store treatment on server
treatment.save()

# Store all dirty (i.e. new or changed) instances of all classes
client.storeAll()

# Create a new child activity and store in the same step
ctangiography=engine.Activity(title="CT Angiography",type="template").save()

# Create a child container
childContainer=engine.ChildrenContainer(ndx="1").save()

# Link treatment to child activity via ChildrenContainer and ChildBinding
# 1. Link treatment to childContainer via link class
treatment.link(Parent2Container,childContainer)

# 2. Link creation can be chained via live created objects and link class labels.
childContainer.link('Container2Binding',engine.ChildBinding(ndx="1").save())\
              .link('Binding2Child',ctangiography)


# Get all Activities
allActivities=engine.Activity.search()

# Get list neighbours of objects
containers=treatment.getNeighbours(Parent2Container)

# Unlink the ChildrenContainer from the treatment
treatment.unlink(Parent2Container,containers[0])

# Unlinking does not automatically delete the previously linked objects
# Delete all ChildrenContainer
for cc in engine.ChildrenContainer.search():
  cc.delete()

# Unlink the ChildBinding from ctangiography and delete it
binding=ctangiography.getNeighbours('Binding2Child')[0]
ctangiography.unlink('Binding2Child',binding)
binding.delete()

# Delete all Activities
for act in engine.Activity.search():
  act.delete()


