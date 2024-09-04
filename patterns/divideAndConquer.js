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
  let middle = Math.floor(minIndex + maxIndex / 2);
  while (minIndex < maxIndex) {
    if (sortedArray[middle] < numberToFind) {
      minIndex = middle + 1;
    } else if (sortedArray[middle] > numberToFind) {
      maxIndex = middle - 1;
    } else {
      return middle;
    }
    middle = Math.floor(minIndex + maxIndex) / 2;
  }
  return sortedArray[middle] == numberToFind ? middle : -1;
};

export { search };
