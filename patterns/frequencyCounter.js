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

const sameMine = (array1, array2) => {
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

const same = (array1, array2) => {
  // check if they have don't have same length
  if (array1.length !== array2.length) {
    return false;
  }
  // create frequency counter objects
  const frequencyCounter1 = {};
  const frequencyCounter2 = {};
  // populate the frequency counter for the array1
  for (let e of array1) {
    frequencyCounter1[e] = (frequencyCounter1[e] || 0) + 1;
  }
  // populate the frequency counter for the array2
  for (let e of array2) {
    frequencyCounter2[e] = (frequencyCounter2[e] || 0) + 1;
  }
  // loop over the frequency counter and check if they have the same frequency and key
  console.log(`frequencyCounter1`, frequencyCounter1);
  console.log(`frequencyCounter2`, frequencyCounter2);
  for (let e in frequencyCounter1) {
    // check if the key is exist
    if (!(e ** 2 in frequencyCounter2)) {
      return false;
    }
    // check if the frequency is equal
    if (frequencyCounter1[e] !== frequencyCounter2[e ** 2]) {
      return false;
    }
  }
  return true;
};

/**
 * validAnagram
 *
 * @param string string1
 * @param string string2
 *
 * if they are not anagram
 * @returns boolean  false
 * if they are anagram
 * @returns boolean true
 *
 *
 */

const validAnagramOld = (string1, string2) => {
  // check the length of the strings
  if (string1.length !== string2.length) {
    return false;
  }
  // create frequency conters for each string
  const frequencyCounter1 = {};
  const frequencyCounter2 = {};

  // loop over to populate them with key and frequencies
  for (let char of string1) {
    frequencyCounter1[char] = (frequencyCounter1[char] || 0) + 1;
  }
  for (let char of string2) {
    frequencyCounter2[char] = (frequencyCounter2[char] || 0) + 1;
  }

  // loop over one of the counters
  for (let key in frequencyCounter1) {
    // check if they have the same key
    if (!(key in frequencyCounter2)) {
      return false;
    }

    // check if they have the same frequency
    if (!(frequencyCounter1[key] == frequencyCounter2[key])) {
      return false;
    }
  }
  return true;
};

const validAnagram = (string1, string2) => {
  // check the length of the strings
  if (string1.length !== string2.length) {
    return false;
  }
  // create frequency conters for only one of the string
  const lookup = {};

  // loop over to populate them with key and frequencies
  for (let char of string1) {
    lookup[char] = (lookup[char] || 0) + 1;
  }
  // loop over one of the string2
  for (let key of string2) {
    // check if they have the same key
    if (!(key in lookup)) {
      return false;
    }

    // dicreament the frequency of the lookup
    lookup[key] = lookup[key] - 1;
    // if it is dicrement below zero, it is not anagram
    if (lookup[key] == -1) {
      return false;
    }
  }
  return true;
};

export { sameMine, same, validAnagram };
