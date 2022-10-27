const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
  [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
  [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
]

function solution(K, N, M, chargers) {
  // solution 함수 `완성
  let data = new Array(N+1).fill(0)
  for (let i = 0; i < chargers.length; i++) {
    data[chargers[i]] = 1
  }
  let s = 1
  let cnt = 0
  while (s<N-K) {
    let check = 1
    for (let j = K; j > 0; j--) {
      if (data[s+j]==1) {
        s = s+j
        cnt +=1
        check = 0
        break
      }
    
    }
    // console.log(s)
    if (check==1) {
      cnt = 0
      break
    }
  }
  console.log(cnt)
  // console.log()
}

for (const input of inputs) {
  
  solution(input[0], input[1], input[2], input[3])
}