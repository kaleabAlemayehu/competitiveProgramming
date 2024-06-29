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

/**
 * countUniqueValues
 * return the number of unique number
 *
 * @param sortedArray @type array
 *
 * @returns number of unique element
 *
 * @example
 * [1,1, 1, 3,3, 3, 3, 4, 4, 4, 5, 5, 8, 9]
 * @returns 6
 * @example
 * [1, 2, 3,4, 5, 6, 6, 6, 7, 8, 9, 10, 11]
 * @returns 11
 */

const countUniqueValues = (sortedArray) => {
  // create pointers
  let i = 0;
  let j = 1;
  // create unique counter

  let unique = 1;
  // loop over the array until i == length - 1
  while (j < sortedArray.length) {
    // check if sortedArray[i] !== sortedArray[j]
    if (sortedArray[i] !== sortedArray[j]) {
      // increment unique
      unique++;
      // make i = j
      i = j;
      // increment j
      j++;
    } else {
      // increment j
      j++;
    }
  }
  return unique;
};

export { sumZero, countUniqueValues };
