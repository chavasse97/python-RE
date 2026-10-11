# graf6
from collections import deque

def findshortestpath(file_name, k, l):
    try:
        with open(file_name, 'r') as file:
            # city amo
            n = int(file.readline().strip())
            
            # m
            matrix = []
            for _ in range(n):
                line = file.readline().strip()
                if line:
                    matrix.append(list(map(int, line.split())))
        
        # 0-ind
        start_vertex = k - 1
        
        # l=1 => path=2
        target_distance = l + 1
        
        # bfs
        queue = deque([(start_vertex, 0)])
        
        # shortest paths lib
        distances = {start_vertex: 0}
        
        # bfs
        while queue:
            current, dist = queue.popleft()
            
            # if >L
            if dist > target_distance:
                continue
                
            # neighbors
            for neighbor in range(n):
                if matrix[current][neighbor] == 1 and neighbor not in distances:
                    distances[neighbor] = dist + 1
                    queue.append((neighbor, dist + 1))
        
        # checker
        result_cities = [i + 1 for i, dist in distances.items() if dist == target_distance]
        
        # out
        if result_cities:
            # sort
            result_cities.sort()
            print(*(result_cities))
        else:
            print(-1)
            
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# launch
findshortestpath('fly.txt', k=1, l=4)
'''
filecomment
if data 1 1 path 1>3>2 possible, but 1>2 exists so it wont be outputted
if data 1 3, 8 has 2 paths 1>2>4>6>8 and 1>3>5>7>8, should be outputted 1 time
if data 1 4 ans will be -1
'''