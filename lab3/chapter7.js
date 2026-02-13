if ("0") {
  alert( 'Привет' ); //yes
}

let name = prompt("Какое официальное название жс: ");
if(name=="ECMAScript"){
    alert("true");
}
else{
    ("false, ECMAScript!");
}

let num = prompt("Your numers is ");
if(num>0){
    alert(1);
}
else if(num<0){
    alert(-1);
}
else{
    alert(0);
}

let a, b;
let result = (a+b<4)?"Мало":"Много";

let message = (login == 'Сотрудник') ? 'Привет' :
  (login == 'Директор') ? 'Здравствуйте' :
  (login == '') ? 'Нет логина' :
  '';