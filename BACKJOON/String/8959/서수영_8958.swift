let caseNum = Int(readLine()!)!

func countScore() -> Int {
    var scoreSum = 0
    readLine()!.split(separator: "X").map({ scoreSum += ($0.count * ($0.count+1) / 2)})
    
    return scoreSum
}

for _ in 0..<caseNum {
    print(countScore())
}
