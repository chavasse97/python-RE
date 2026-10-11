# graf10
def find_all_routes(input_file, output_file, k1, k2):
    try:
        # read
        with open(input_file, 'r') as file:
            n = int(file.readline().strip())
            matrix = []
            for _ in range(n):
                line = file.readline().strip()
                if line:
                    matrix.append(list(map(int, line.split())))
        
        # 0-ind
        start = k1 - 1
        end = k2 - 1
        
        all_paths = []
        
        # dfs
        def dfs(current_vertex, current_path, visited):
            # save if end
            if current_vertex == end:
                all_paths.append(list(current_path))
                return
            
            # everyflight
            for neighbor in range(n):
                if matrix[current_vertex][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    current_path.append(neighbor)
                    
                    dfs(neighbor, current_path, visited)
                    
                    # backtracking
                    current_path.pop()
                    visited.remove(neighbor)

        # launch dfs
        dfs(start, [start], {start})
        
        # saving
        with open(output_file, 'w') as out_file:
            if not all_paths:
                out_file.write("-1\n")
            else:
                # sort by length then lexic
                all_paths.sort(key=lambda x: (len(x), x))
                
                # path amo
                out_file.write(f"{len(all_paths)}\n")
                
                # paths 1-ind
                for path in all_paths:
                    readable_path = [vertex + 1 for vertex in path]
                    out_file.write(" ".join(map(str, readable_path)) + "\n")
                    
    except FileNotFoundError:
        print(f"'{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# launch
find_all_routes('fly.txt', 'flyout.txt', k1=1, k2=8)
print("Done")
'''
1 8
should find 1>2 1>3>2 and 2 more paths
'''