from collections import deque

def waterJugProblem(capacity1, capacity2, goal):
    queue = deque()
    visited = set()
    queue.append((0, 0))
    visited.add((0, 0))
    actions = []
    
    while queue:
        jug1, jug2 = queue.popleft()
        actions.append((jug1, jug2))
        
 
        if jug1 == goal or jug2 == goal:
            print("Solution Found")
            for action in actions:
                print(action)
            return True
        

        rules = [
           (capacity1, jug2),  # 1: Fill Jug1
           (jug1, capacity2),  # 2: Fill Jug2
           (0, jug2),  # 3: Empty Jug1
           (jug1, 0),  # 4: Empty Jug2
           (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)),  # 5: Pour Jug1 -> Jug2 until full or empty
           (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1)),  # 6: Pour Jug2 -> Jug1 until full or empty
        ]
        
        for idx, state in enumerate(rules, 1):
            if state not in visited:
                print(f"Rule {idx}: {state}")  
                visited.add(state)
                queue.append(state)

    print("No Solution found")
    return False


if __name__ == "__main__":
    jug1Capacity = 4
    jug2Capacity = 3
    target = 2          
    waterJugProblem(jug1Capacity, jug2Capacity, target)
