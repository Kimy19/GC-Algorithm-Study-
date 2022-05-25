//
//  main.swift
//  BOJ
//
//  Created by 서수영 on 2022/05/24.
//

import Foundation

// 1 <= N, M <= 100,000, 존재하면 1 없으면 0

let N = Int(readLine()!)!
let A: [Int] = readLine()!.split(separator: " ").map{ Int($0)!}.sorted()

let M = Int(readLine()!)!
let B: [Int] = readLine()!.split(separator: " ").map { Int($0)!}

//print(A, B)
func binarySearch(v: Int) -> Bool {
    var upperBound = A.count
    var lowerBound = 0
    
    
    while upperBound != lowerBound {
        var mid = (upperBound+lowerBound)/2
        if lowerBound>=A.count || upperBound<=0{return false}
        
        
        //print("mid \(mid)" )
        if v > A[mid]{
            //print(v, A[mid], mid, lowerBound, upperBound, "lowerbound")
            lowerBound = mid+1
        }else if v < A[mid]{
            //print(v, A[mid], mid, lowerBound, upperBound, "upperbound")
            upperBound = mid
        }else{
            return true
        }
    }
    return false
}

for b in B{
    //print(b, binarySearch(v: b))
    binarySearch(v: b) ? print(1) : print(0)
}
