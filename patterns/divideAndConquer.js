/**
 *
 * @function search
 * @param sortedArray @type Array<Int>
 * @param numberToFind @type Number
 * @returns indexOfTheNumber @type Number
 */

const search = (sortedArray, numberToFind) => {
  let minIndex = 0,
    maxIndex = sortedArray.length - 1;
  while (minIndex <= maxIndex) {
    let middle = Math.floor(minIndex + maxIndex / 2);
    if (sortedArray[middle] < numberToFind) {
      minIndex = middle + 1;
    } else if (sortedArray[middle] > numberToFind) {
      maxIndex = middle - 1;
    } else {
      return middle;
    }
  }
  return -1;
};

export { search };
