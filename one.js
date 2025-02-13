function MathChallenge(num1, num2) { 
 
    let ans = Math.round(num1 / num2)
    let formattedAns = ans.toLocaleString()
    let reversed = formattedAns.split('').reverse().join()
   
    let challengeToken = "tdaospy613"
    let reversedToken = challengeToken.split('').reverse().join('')
    return `${reversed}:${reversedToken}`; 
   
  }
     
  // keep this function call here 
  console.log(MathChallenge(readline()));