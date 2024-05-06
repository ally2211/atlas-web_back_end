export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length); // Creates an ArrayBuffer of 16 bytes
  // Create a DataView that references the ArrayBuffer
  const dataView = new DataView(buffer);
  const int8View = new Int8Array(buffer); // Creates an Int32Array view of the buffer
  int8View[position] = value;
  return dataView;
}
