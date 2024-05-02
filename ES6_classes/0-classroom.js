// Define the constructor function
function ClassRoom(maxStudentsSize) {
    this._maxStudentsSize = maxStudentsSize; // Private-like property
}

// Add a method to the prototype to describe the classroom capacity
ClassRoom.prototype.describeCapacity = function() {
    return `This classroom can accommodate up to ${this._maxStudentsSize} students.`;
};

// Export the ClassRoom as default
export default ClassRoom;
