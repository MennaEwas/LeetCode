class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set() 
        stack = [0]
        while stack:
            room = stack.pop()
            visited.add(room)
            for k in rooms[room]:
                if k not in visited:
                    stack.append(k)
        return len(visited) == len(rooms)