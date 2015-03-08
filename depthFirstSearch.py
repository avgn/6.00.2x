def depthFirstSearch(tree, target):
    open = []
    closed = []
    open.append()
    while open not == []:
        if open[0] == target:
            closed.append(open[0])
            break
        else:
            insert(0, open[0].getRightBranch)
            insert(0, open[0].getLeftBranch)
            closed.append(open[0])
    return closed