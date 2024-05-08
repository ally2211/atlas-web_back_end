// utils.js
export function uploadPhoto() {
 // Simulate an asynchronous operation
 return new Promise((resolve) => {
   resolve({
     status: 200,
     body: 'photo-profile-1',
   });
 });
}

export function createUser() {
 // Simulate an asynchronous operation
 return new Promise((resolve) => {
   resolve({
     firstName: 'Guillaume',
     lastName: 'Salva',
   });
 });
}
