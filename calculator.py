# This matrix is just an example. You can change it
matrix = [
    [0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0]
]

def clustering_coefficient(matrix, ith_element):
    '''
    The function returns the clustering coefficient of the ith element of the 
    adjacency matrix
    '''
    # Calculate the degree k
    k = 0
    for line in matrix:
        k += line[ith_element-1]

    # List of connections: nodes connected to ith_element
    list_of_connections = []
    for i, line in enumerate(matrix):
        if line[ith_element-1] == 1:
            list_of_connections.append(i)  # Use index directly (0-based)
    
    # Calculate l: count edges between neighbors
    l = 0
    for i in list_of_connections:
        for j in list_of_connections:
            if i != j and matrix[i][j] == 1:
                l += 1

    # Each edge is counted twice, so divide by 2
    l = l/2

    # Calculate the clustering coefficient
    try:
        coefficient = 2 * l / (k * (k - 1))
    except ZeroDivisionError:
        coefficient = 0

    return coefficient

def average_clustering_coefficient(matrix):
    '''
    The function returns the average clustering coefficient of the matrix
    '''
    total = 0
    for i, _ in enumerate(matrix):
        total += clustering_coefficient(matrix, i + 1)
    avrg = total / len(matrix)
    return avrg
