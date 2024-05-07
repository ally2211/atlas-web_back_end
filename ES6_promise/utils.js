// utils.js
export function uploadPhoto() {
 // Simulate an asynchronous operation
 return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ body: 'photo-profile-1' });
    }, 1000);
 });
}

export function createUser() {
 // Simulate an asynchronous operation
 return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ firstName: 'Guillaume', lastName: 'Salva' });
    }, 1000);
 });
}
