let i = 3;

while (i) {
  alert( i-- );
} //1

let i2 = 0;
while (++i2 < 5) alert( i2 ); //1 2 3 4

let i3 = 0;
while (i3++ < 5) alert( i3 ); //1 2 3 4 5

for (let i = 0; i < 5; i++) alert( i ); // 0 1 2 3 4
for (let i = 0; i < 5; ++i) alert( i ); // 0 1 2 3 4

for (let i = 2; i <= 10; i++) {
  if (i % 2 == 0) {
    alert( i );
  }
}

for (let i = 0; i < 3; i++) {
  alert( `number ${i}!` );
}

let num;

do {
  num = prompt("Введите число больше 100?", 0);
} while (num <= 100 && num);

let n = 10;

nextPrime:
for (let i = 2; i <= n; i++) {

  for (let j = 2; j < i; j++) { 
    if (i % j == 0) continue nextPrime; 
  }

  alert( i ); 
}

