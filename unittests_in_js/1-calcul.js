function calculateNumber(type, a, b) {
  arg1 = Math.round(a);
  arg2 = Math.round(b); 

  switch(type) {
    case 'SUM':
      return (arg1 + arg2);
    break;

    case 'SUBTRACT':
      return(arg1 - arg2);
    break;
    
    case 'DIVIDE':
      return arg2 !== 0? arg1 / arg2: 'Error';
    break;

    default: 
    return Error('Parameter type erroned!');
  }
}

module.exports = { calculateNumber };
