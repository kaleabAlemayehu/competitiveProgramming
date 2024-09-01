/**
 *
 * @function maxSubArraySum
 * @param arrayOfNumbers @type Array<Int>
 * @param numbersOfDigit @type Number
 * @returns maxSum @type Number
 */

const maxSubArraySum = (arrayOfNumbers, numbersOfDigit) => {
  // tackle edge cases
  if (arrayOfNumbers.length < numbersOfDigit) {
    return null;
  }
  // temporary maxSum
  let tempSum = 0;
  for (let i = 0; i < numbersOfDigit; i++) {
    tempSum += arrayOfNumbers[i];
  }
  //   store tempsum on maxSum
  let maxSum = tempSum;
  //   then by comparing the tempsum with maxSum get the real maxsum
  for (let i = 0; i < arrayOfNumbers.length - numbersOfDigit; i++) {
    tempSum = tempSum - arrayOfNumbers[i] + arrayOfNumbers[i + numbersOfDigit];
    maxSum = Math.max(tempSum, maxSum);
  }
  return maxSum;
};

export { maxSubArraySum };
// [1, 2, 3, 4, 2, 5, 2, 3] => 4
