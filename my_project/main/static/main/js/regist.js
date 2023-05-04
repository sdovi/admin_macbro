function checkform(el) {
    var phone = el.phone.value
    var name = el.name.value
    var surname = el.surname.value

    error = "";
    if (phone == "" || name == "" || surname == "") {
        error = "Дополните все пункты";
    }
    else if (phone.length <= 9  ) {
        error = "Недостаточно символов";
    }
    else if (phone.length >= 14){
        error = "Не существует такого номера"
    }
    else if (name.length <= 2) {
        error = "Введите корректное имя";
    }
    else if (surname.length <= 2) {
        error = "Введите корректное фамилию";
    }

    if (error != '') {
        document.getElementById('field').innerHTML = error;
        return false
    }
    else {
        alert("Успешно зарегистрировались!")
        return true
    }
    
}
var text = document.getElementById("123");
console.log(text.class);