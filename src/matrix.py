matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

reverse_matrix = map(reversed, matrix)


def rrotate_matrix(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]


def lrotate_matrix(matrix):
    return [list(col) for col in zip(*map(reversed, matrix))]


if __name__ == '__main__':
    print(*matrix, sep='\n')
    print('-------------')
    ans = rrotate_matrix(matrix)
    print(*ans, sep='\n')
    print('-------------')
    ans = lrotate_matrix(matrix)
    print(*ans, sep='\n')
    print('-------------')
