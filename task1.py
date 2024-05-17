class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def construct_tree_from_preorder(preorder):
    if not preorder:
        return None

    val = preorder.pop(0)
    if val == 0:
        return None

    node = TreeNode(val)
    node.left = construct_tree_from_preorder(preorder)
    node.right = construct_tree_from_preorder(preorder)

    return node


def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


def rebuild_binary_search_tree(root, values):
    if root is None:
        return

    # Використовуємо ітератор для значень, щоб не обрізати список values
    val_iter = iter(values)

    # Рекурсивно перебудовуємо дерево пошуку, вставляючи значення зі списку values
    rebuild_binary_search_tree_helper(root, val_iter)


def rebuild_binary_search_tree_helper(node, val_iter):
    if node is None:
        return

    # Перебудова лівого піддерева
    rebuild_binary_search_tree_helper(node.left, val_iter)

    # Оновлення значення поточного вузла
    node.val = next(val_iter)

    # Перебудова правого піддерева
    rebuild_binary_search_tree_helper(node.right, val_iter)


def read_preorder_from_file(filename):
    with open(filename, 'r') as f:
        preorder = list(map(int, f.read().split()))
    return preorder


# Основна частина програми

def transformToBinarySearchTree(input_file: str):
    # Зчитуємо preorder з файлу
    preorder = read_preorder_from_file(input_file)

    # Побудова бінарного дерева з preorder
    root = construct_tree_from_preorder(preorder)

    # Побудова inorder з урахуванням нулів
    inorder_values = sorted(
        set(val for val in inorder_traversal(root) if val != 0))

    # Перебудова дерева пошуку
    rebuild_binary_search_tree(root, inorder_values)

    return root