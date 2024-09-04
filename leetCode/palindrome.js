const isPalindromeWithString = function (x) {
  let value = `${x}`;
  let newValue = Array.from(value).reverse().join("");

  return newValue == value ? true : false;
};
const isPalindromeRec = (str) => {
  if (str.length <= 1) return true;
  const helper = (s) => {
    if (s.length <= 1) return s;
    return helper(s.slice(1)) + s[0];
  };
  return str === helper(str);
};

console.log(isPalindromeRec("cat"));
console.log(isPalindromeRec("oo"));

const isPalindrome = (x) => {
  if (x < 0) {
    return false;
  }
  let original = x,
    reverse = 0;
  while (original != 0) {
    reverse = reverse * 10 + (original % 10);
    original = Math.floor(original / 10);
  }
  return x == reverse ? true : false;
};

export { isPalindromeWithString, isPalindrome };
