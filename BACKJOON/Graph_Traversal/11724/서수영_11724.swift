import Foundation

let nmList = readLine()!.split(separator: " ").map( { Int($0)! })
let N = nmList[0]
let M = nmList[1]

var graph: [Int:[Int]] = [:]


for _ in 0..<M{
    let uvList = readLine()!.split(separator: " ").map( { Int($0)! })
    
    let u = uvList[0]
    let v = uvList[1]
    
    (graph[u] != nil) ? (graph[u]!.append(v)) : (graph[u] = [v])
    (graph[v] != nil) ? (graph[v]!.append(u)) : (graph[v] = [u])
}

//print(graph)
func DFS(graph: [Int:[Int]]) -> Int {
    var visited = Array<Int>()
    var needVisit = Array<Int>()
    var rc = 0
    
    for key in graph.keys {
        if visited.contains(key) {continue}
        rc += 1
        
        needVisit.append(key)
        
        while !needVisit.isEmpty{
            let node = needVisit.removeLast()
            if visited.contains(node) {continue}
            
            visited.append(node)
            needVisit += graph[node]!
        }
    }
    
    rc += (N - graph.keys.count)
    //간선에 포함 되지 않은 노드들도 하나의 연결요소로 계산
    return rc
}

print(DFS(graph: graph))
