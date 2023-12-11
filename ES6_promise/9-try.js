export default function guardrail(mathFunction) {
  let queue = ['Guardrail was processed'];
  let message = '';

  try {
    message = mathFunction();
  } catch (err) {
    message = err;
  }

  queue.unshift(message);
  return queue;
}