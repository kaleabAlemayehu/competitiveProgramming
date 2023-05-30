const isPalindromeWithString = function (x) {
  let value = `${x}`;
  let newValue = Array.from(value).reverse().join("");

  return newValue == value ? true : false;
};

export { isPalindromeWithString };
