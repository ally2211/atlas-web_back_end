export default function loadBalancer(chinaDownload, USDownload) {
  return Promise.all([chinaDownload, USDownload]).then(() => {
    chinaDownload.then((chinaResult) => {
      console.log(chinaResult);
      // After logging the result of the first promise, execute the second promise
      USDownload.then((USResult) => {
        console.log(USResult);
      });
    });
  }).catch((error) => {
    console.log('Signup system offline', error);
  });
}
