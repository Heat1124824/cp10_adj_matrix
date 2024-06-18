def adj_mat(edges, num_vertices):
    adj_matrix = [[0]*num_vertices for row in range(num_vertices)]
    for i in range(len(edges)):
        tmpi = edges[i][0]
        tmpj = edges[i][1]
        adj_matrix[tmpi][tmpj] = 1

    return adj_matrix

def degree_of_vertex(matrix, vertex):
    degree = 0
    for i in range(len(matrix)):
        degree += matrix[vertex][i]
    return degree

def main():
    num_vertices = 5
    edges = [[0, 1], [1, 0],
             [0, 3], [3, 0],
             [1, 4], [4, 1],
             [2, 4], [4, 2]]
    matrix = adj_mat(edges, num_vertices)

    for i in range(num_vertices):
        for j in range(num_vertices):
            print('%d ' % matrix[i][j], end='')
        print() 

    for i in range(num_vertices):
        degree = degree_of_vertex(matrix, i)
        print("頂點", i, "分支度為:", degree)

if __name__ == "__main__":
    main()