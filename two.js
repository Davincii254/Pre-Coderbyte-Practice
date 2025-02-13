function ArrayChallenge(arr) { 
    let [a, b, c, d, x] = arr
   
    let firstRange = new Set(Array.from({ length: b - a + 1}, (_, i) => a + i)) 
    let secondRange = new Set(Array.from({ length: d - c + 1}, (_, i) => c + i))
   
    let overlapping = [...firstRange].filter(num => secondRange.has(num))
   
    return overlapping.length >= x ? "true" : "false"; 
   
  }
     
  // keep this function call here 
  console.log(ArrayChallenge(readline()));