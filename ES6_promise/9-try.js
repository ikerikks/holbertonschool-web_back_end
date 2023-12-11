export default function guardrail(mathFunction) {
  const queue = ['Guardrail was processed'];
  let message = '';

  try {
    message = mathFunction();
  } catch (err) {
    message = String(err);
  }

  queue.unshift(message);
  return queue;
}
