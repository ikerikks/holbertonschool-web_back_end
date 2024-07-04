const calculateNumber = (a, b) =>  {
  arg1 = Math.round(Math.abs(a)) * Math.sign(a);
  arg2 = Math.round(Math.abs(b)) * Math.sign(b);
  return Math.round(arg1 + arg2);
}
module.exports = calculateNumber;

