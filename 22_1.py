# graf1
def solve(file_name):
    try:
        with open(file_name, 'r') as file:
            # n
            n = int(file.readline().strip())
            
            # m
            matrix = []
            for _ in range(n):
                line = file.readline().strip()
                if line:
                    matrix.append(list(map(int, line.split())))
            
            # degrees
            for i in range(n):
                degree = 0
                for j in range(n):
                    if matrix[i][j] > 0:
                        # i=j x2
                        if i == j:
                            degree += matrix[i][j] * 2
                        else:
                            degree += matrix[i][j]
                
                print(f"Vertex {i + 1}: degree {degree}")
                
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except ValueError:
        print("Incorrect data format.")

# launch
solve('graph.txt')
