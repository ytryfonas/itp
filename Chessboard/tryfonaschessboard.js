let b = ''; // board variable  
const size = 8; // size of board

for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
        if ((i + j) % 2 === 0) {
            b += ' ';
        } else {
            b += '#';
        }
    }
    b += '\n';
}

console.log(b);
