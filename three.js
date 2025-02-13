function SearchingChallenge(str) { 
    let charCount = {}
   
    for (let char of str) {
      if (char != " "){
        charCount[char] = (charCount[char] || 0) + 1
      }
    }
    let NonRepeating = ""
    for (let char of str){
      if (char !== " " && charCount[char] === 1) {
        NonRepeating = char
        break
      }
    }
    let challengeToken = "tdaospy613"
    let finishedAns = `${NonRepeating.split('').reverse().join('')}: ${challengeToken.split('').reverse().join('')}`
    return finishedAns; 
   
  }
     
  // keep this function call here 
  console.log(SearchingChallenge(readline()));