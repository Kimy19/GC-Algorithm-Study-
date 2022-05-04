import Foundation


//str1 str2
let num: Int = Int(readLine()!)!


for i in 0..<num{
    let testString: [String]? = readLine()?.components(separatedBy: .whitespaces)
    
    let result = testAnagram(testString![0], testString![1]) ? "Yes" : "No"
    print(String(format: "case%d: %@", i+1, result))
}

func testAnagram(_ testStr1: String, _ testStr2: String) -> Bool {

    //1. 개수 체크
    guard testStr1.count == testStr2.count else{return false}

    //2.정렬 이후 같은지 체크
    guard testStr1.sorted() == testStr2.sorted() else{return false}

    //3. 1,2에서 안걸러졌으면 아나그램
    return true
}
