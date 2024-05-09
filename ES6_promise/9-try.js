export default function guardrail(mathFunction) {
  const queue = [];
  return new Promise((resolve, reject) => {
    if (mathFunction) {
      queue.append('Guardrail was processed');
      // Resolve the promise with an object
      resolve({
        queue,
      });
    } else {
      // Reject the promise with an error
      reject(new Error(queue.append('Error: cannot divide by 0')));
    }
  });
}
