/**
 *
 * function called same
 *
 *
 * accept 2 arrays
 * @param {*} array1
 * @param {*} array2
 *
 * if every value in the array has corresponding number who is squared of it self && the frequency must be the same
 *      return true
 *
 * else
 *  return false
 *
 *
 */

/**
 *
 *  example input
 * array1 = [1, 2, 3], array2 = [4, 1, 9] return true
 * array1 = [1, 2, 3], array2 = [1 ,9] return false
 * array1 = [1, 2, 1], array2 = [4, 4, 1] return false
 *
 */

const same = (array1, array2) => {
  // check if the have the same length
  if (array1.length === array2.length) {
    // loop over the first array
    for (let e of array1) {
      // store the square of the element
      let ex = Math.pow(e, 2);
      // check if it has the corresponding squre element
      if (array2.includes(ex)) {
        // if it has remove the element from the second array {hint: to apply the frequency} precide to the next
        array2.splice(array2.indexOf(ex), 1);
      } else {
        // if it has not return false
        return false;
      }
    }
    // after finishing the loop return true
    return true;
  }
  // if they don't have the same length return false
  return false;
};

export { same };
