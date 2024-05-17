import sys
import os
from task1 import transformToBinarySearchTree


def find_paths_with_sum(root, target_sum, current_path, result):
    if root is None:
        return

    # Додаємо поточний вузол до поточного шляху
    current_path.append(root.val)

    # Якщо значення поточного шляху дорівнює цільовій сумі, додаємо його до результату
    if sum(current_path) == target_sum:
        result.append(list(current_path))

    # Рекурсивно шукаємо вліво та вправо
    find_paths_with_sum(root.left, target_sum, current_path, result)
    find_paths_with_sum(root.right, target_sum, current_path, result)

    # Після проходження вузла видаляємо його з поточного шляху
    current_path.pop()


def find_all_paths_from_node(node, target_sum, result):
    if node is None:
        return

    # Запускаємо пошук шляхів з поточного вузла
    find_paths_with_sum(node, target_sum, [], result)

    # Рекурсивно запускаємо пошук для лівого та правого піддерева
    find_all_paths_from_node(node.left, target_sum, result)
    find_all_paths_from_node(node.right, target_sum, result)


def find_all_paths_with_sum(root, target_sum):
    if root is None:
        return []

    result = []
    find_all_paths_from_node(root, target_sum, result)
    print(result)
    return result


def write_tree_and_paths_to_file(root, paths, filename):
    with open(filename, 'w') as f:
        # Запис бінарного дерева пошуку
        write_tree_to_file(root, f)

        # Роздільник між бінарним деревом та шляхами
        f.write("\nPaths with sum:\n")

        # Запис шляхів у файл
        for path in paths:
            f.write(' '.join(map(str, path)) + '\n')


def write_tree_to_file(root, filey):
    if root is None:
        filey.write("0 ")
        return
    filey.write(str(root.val) + " ")
    write_tree_to_file(root.left, filey)
    write_tree_to_file(root.right, filey)


# Основна частина програми
directory = "D:\\КПІ\\ТА. Лабораторні\\TA.Lab6"
inputDir = "\\examples"
outputDir = "\\results"


def cycle(input_file: str, output_file: str, target_sum: int):
    root = transformToBinarySearchTree(input_file)

    # Знаходимо всі монотонні шляхи з сумою target_sum
    monotonic_paths = find_all_paths_with_sum(root, target_sum)

    # Запис бінарного дерева та шляхів у файл
    write_tree_and_paths_to_file(root, monotonic_paths, output_file)


if __name__ == "__main__":
    cycle(directory+inputDir+"\\input_1000c.txt",
          directory+outputDir+"\\output_1000c.txt", 513)
else:
    # Основна частина програми
    if len(sys.argv) != 4:
        print("Потрібно ввести ім'я вхідного файлу, ім'я вихідного файлу та число S як аргументи командного рядка.")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    target_sum = int(sys.argv[3])

    # Перевірка наявності вхідного файлу
    if not os.path.exists(input_file):
        print("Вхідний файл не знайдено.")
        sys.exit(1)

    cycle(input_file, output_file, target_sum)

# python "D:\КПІ\ТА. Лабораторні\TA.Lab6\task2.py" "D:\КПІ\ТА. Лабораторні\TA.Lab6\examples\input_10a.txt" "D:\КПІ\ТА. Лабораторні\TA.Lab6\results\output_10a.txt" 9
