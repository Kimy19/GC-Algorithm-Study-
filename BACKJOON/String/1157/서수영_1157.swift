import Foundation

//let caseCount = Int(readLine()!)!
let caseCount = 1

func findMostUsed(_ testChrArr: [Character] ) -> Character {
    var dct: [Character:Int] = [:]
    var result: [Character] = []
    
    for testChr in testChrArr {
        if dct[testChr] == nil {
            dct[testChr] = 1
        } else{
            dct[testChr]! += 1
        }
    }
    
    for k in dct.keys{
        if dct.values.max() == dct[k]{
            result.append(k)
        }
    }
    
    return (result.count > 1 ? "?" : result[0])
}


for _ in 0..<caseCount {
    let testCase = readLine()!.uppercased().map( {$0} )
    print(findMostUsed(testCase))

}
