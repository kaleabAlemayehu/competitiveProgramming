var createCounter = function (n) {
  return function () {
    return n++;
  };
};

export { createCounter };
