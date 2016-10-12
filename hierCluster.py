from distance import *
import sys

class treeNode:
    def __init__(self, vec, left=None, right=None, distance=0.0, id=None):
        self.left = left
        self.right = right
        self.vec = vec
        self.distance = distance
        self.id = id

def buildTree(data, dist_measure=pearson):
    distance = {}
    num_sample = len(data)
    current_id = -1

    cluster = set([treeNode(data[i], id=i) for i in range(num_sample)])

    while len(cluster) > 1:
        closest_dist = sys.float_info.max 
        closest_pair = (None, None)

        # find the closest node pair in the tree
        for node1 in cluster:
            for node2 in cluster:
                if node1.id == node2.id:
                    continue

                if node1.id < node2.id:
                    key = (node1.id, node2.id)
                else:
                    key = (node2.id, node1.id)

                if key not in distance:
                    distance[key] = dist_measure(node1.vec, node2.vec)

                d = distance[key]
                if d < closest_dist:
                    closest_dist = d
                    closest_pair = (node1, node2)

        # merge the closest node pair
        avg_vec = [(xi + yi) / 2.0 for xi, yi in \
                zip(node1.vec, node2.vec)]

        new_node = treeNode(avg_vec, left=closest_pair[0], 
                right=closest_pair[1], distance=closest_dist,
                id=current_id)

        current_id -= 1
        cluster.remove(closest_pair[0])
        cluster.remove(closest_pair[1])
        cluster.add(new_node)
        del distance[key]

    return cluster.pop()


def displayTree(root, label, degree=0):
    if not root:
        return

    if root.id >= 0:
        print('  ' * degree + label[root.id])
    else:
        print('  ' * degree + '--')

    degree += 1
    if root.left:
        displayTree(root.left, label, degree)
    if root.right:
        displayTree(root.right, label, degree)
        


                    


        


