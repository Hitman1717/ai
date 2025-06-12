def build_tree(leaves, branching_factor, depth):
    if depth == 0:
        return leaves.pop(0)
    tree = []
    for _ in range(branching_factor):
        subtree = build_tree(leaves, branching_factor, depth - 1)
        tree.append(subtree)
    return tree

def alpha_beta(tree, alpha, beta, is_maximizer):
    if isinstance(tree, int):
        return tree

    if is_maximizer:
        value = float('-inf')
        for child in tree:
            value = max(value, alpha_beta(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in tree:
            value = min(value, alpha_beta(child, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break 
        return value


depth = int(input('Enter the Depth:\t'))
print(f"You have to enter {2**depth} numbers")
l = list(input().split(sep=" "))
l = [ int(i) for i in l]
tree = build_tree(l.copy(),2,depth)
print(tree)
print(alpha_beta(tree , -10000, 10000 , True))
