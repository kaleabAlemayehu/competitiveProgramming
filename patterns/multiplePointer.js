/**
 * sum zero
 * for a give sorted array sortedArray
 *
 * return the first pair of element where sum of them is zero
 * @var i
 * @var j
 * @returns [sortedArray[i] + sortedArray[j] == 0]
 * @param sortedArray
 *
 * @example example1
 * [-3, -2, -1, 0, 1, 2, 3]
 *
 *
 *
 * @returns [-3, 3]
 *
 */

const sumZero = (sortedArray) => {
  let i = 0;
  let j = sortedArray.length - 1;
  while (i < j) {
    let sum = sortedArray[i] + sortedArray[j];
    if (sum == 0) {
      return [sortedArray[i], sortedArray[j]];
    } else if (sum < 0) {
      i++;
    } else {
      j--;
    }
  }
  return undefined;
};

export { sumZero };
