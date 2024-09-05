import heapq
from typing import List, Tuple
from tile.tile import Tile


def findPath(graph: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]):
    """
    다익스트라 알고리즘을 이용하여 최단 경로를 찾고, 이동 경로를 반환하는 함수

    Args:
        graph: 2차원 리스트로 표현된 맵
        start: 시작 노드 (x, y) 튜플
        goal: 목표 노드 (x, y) 튜플

    Returns:
        최단 경로의 총 비용, 이동 경로 (리스트)
    """
    rows, cols = len(graph), len(graph[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 상, 하, 좌, 우 방향만 고려

    # 초기화
    distances = [[float("inf")] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    visited = [[False] * cols for _ in range(rows)]
    parents = [[None] * cols for _ in range(rows)]
    heap = [(0, start)]

    while heap:
        current_distance, (x, y) = heapq.heappop(heap)

        if visited[x][y]:
            continue

        visited[x][y] = True

        for dx, dy in directions:
            newX, newY = x + dx, y + dy
            if 0 <= newX < rows and 0 <= newY < cols and not visited[newX][newY]:
                new_distance = current_distance + graph[newX][newY] + 1
                if new_distance < distances[newX][newY]:
                    distances[newX][newY] = new_distance
                    parents[newX][newY] = (x, y)
                    heapq.heappush(heap, (new_distance, (newX, newY)))

    # 경로 복원
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parents[current[0]][current[1]]
    path.append(start)
    path.reverse()

    return distances[goal[0]][goal[1]], path


def convertToGraph(mapData: List[List[Tile]]) -> List[List[int]]:
    """
    타일 맵 데이터를 그래프로 변환하는 함수

    Args:
        mapData: 타일 맵 데이터

    Returns:
        그래프
    """
    graph = []
    for row in mapData:
        graph.append([0 if tile.tile != "water" else -1 for tile in row])
    return graph
