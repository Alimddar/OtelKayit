const inputs = document.getElementsByTagName('input');
const labels = document.getElementsByTagName('label');

for (let i = 0; i < labels.length; i++) {
    const label = labels[i];
    label.classList.add('form-label');
    
    // Yeni div oluştur
    const div = document.createElement('div');
    div.classList.add("mb-3");
    
    // Labellerı divin içine taşı
    label.parentElement.insertBefore(div, label);
    div.appendChild(label);
    
    // İlgili inputu bul
    for (let j = 0; j < inputs.length; j++) {
        if (inputs[j].type == 'text' || inputs[j].type == 'number') {
            inputs[j].classList.add('form-control');
            
            // İlgili label ile inputu bir araya getir
            if (label.htmlFor === inputs[j].id) {
                label.parentElement.insertBefore(inputs[j], label.nextSibling);
            }
        } else if (inputs[j].type == 'checkbox') {
            inputs[j].classList.add('form-check-input','ms-2');
            
            // İlgili label ile inputu bir araya getir
            if (label.htmlFor === inputs[j].id) {
                label.parentElement.insertBefore(inputs[j], label.nextSibling);
            }
        }
    }
}