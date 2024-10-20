export default function calculateNumber(type, a, b){
    const roundedA = Math.round(a);
    const roundedB = Math.round(b);
    if (type === 'SUM') {
        return Math.round(a) + Math.round(b);
    }
    else if (type === 'SUBTRACT') {
        return Math.round(a) - Math.round(b);
    }
    else if (type === 'DIVIDE') {
        if (Math.round(b) === 0) {
            throw new Error('Cannot divide by zero');
        
        // Round the result of the division to one decimal place
        return Math.round((roundedA / roundedB) * 10) / 10;
        }
    }
    else {
        throw new Error('Invalid operation type');
    }
}
