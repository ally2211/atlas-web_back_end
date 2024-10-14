// Prompt for name if input is interactive
if (process.stdin.isTTY) {
   process.stdout.write("Welcome to Atlas School, what is your name? \n");
}
// Listen for data from stdin (user input)
process.stdin.on("data", (data) => {
    const name = data.toString().trim();  // Convert input to string and remove extra whitespace
    console.log(`Your name is: ${name}`); // Display the input
    
    // If input is piped, simulate a SIGINT signal
    if (!process.stdin.isTTY) {
        handleSigint();;
    }
    else {
        process.exit(); 
    }
});

// Listen for 'SIGINT' signal (Ctrl + C)
function handleSigint() {
    console.log("This important software is now closing");
    process.exit(); // Exit the process gracefully
}
