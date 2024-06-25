export function calculateNumber(type, a, b) {
  let result = '';
  switch(type) {
    case 'SUM':
      result = Math.ceil(a + b);
    break;

    case 'SUBTRACT':
      result = ((a - b) >= 0 || -1) * 
      Math.ceil(Math.abs(a - b));
    break;
    
    case 'DIVIDE':
      result = Math.round((a / b) * 10) / 10 ;
    break;
  }
  return result == Infinity || isNaN(result)?
    'Error': result;
}

