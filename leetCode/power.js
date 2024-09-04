const power = (base, exponent) => {
  if (exponent == 0 && base != 0) return 1;
  if (exponent == 0 && base == 0) return undefined;
  return base * power(base, exponent - 1);
};

console.log(power(-3, 3));
