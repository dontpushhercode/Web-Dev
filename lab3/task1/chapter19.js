let str = "Привет";

str.test = 5; // (*)

alert(str.test); //undefined (без strict) || Ошибка (strict mode)