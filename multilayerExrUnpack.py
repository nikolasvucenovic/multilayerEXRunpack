import nuke

def shuffleLayer(node, layer):

    shuffleNode = nuke.nodes.Shuffle(label=layer, inputs=[node])
    shuffleNode['in'].setValue(layer)
    shuffleNode['postage_stamp'].setValue(True)
    return shuffleNode

node = nuke.selectedNode()

def shuffleAllLayers(node):
    channels = node.channels()
    layers = list(set([c.split('.')[0] for c in channels]))
    layers.sort()
    
    for layer in layers:
        shuffleLayer(node, layer)

shuffleAllLayers(node)
