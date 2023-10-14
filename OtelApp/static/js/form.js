const input = document.getElementsByTagName('input');
const label = document.getElementsByTagName('label');


for(let i = 0; i < label.length; i++ ){
    label[i].classList.add('form-label')
    // Yeni div oluştur
    const div = document.createElement('div');
    div.classList.add("mb-3");
    // Labellerı divin içine taşı
    label[i].parentElement.insertBefore(div, label[i]);
    div.appendChild(label[i])
}


for(let i = 0; i < input.length; i++){
    if(input[i].type == 'text' || input[i].type == 'number'){
        input[i].classList.add('form-control')
    }else if (input[i].type == 'checkbox'){
        input[i].classList.add('form-check-input')
    }
}