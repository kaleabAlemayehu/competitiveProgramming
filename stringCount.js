const stringCount = (longString, subString) => {
  let count = 0;
  let j = 0;
  for (let i = 0; i < longString.length; i++) {
    for (j = 0; j < subString.length; j++) {
      if (longString[i] !== subString[j]) {
        break;
      } else {
        if (longString[i + 1] !== subString[j]) i++;
      }
    }
    if (j == subString.length) {
      count++;
    }
  }

  return count;
};
//      hong kong
//           kong

console.log(stringCount("substringforti sssstring string", "string"));
