const inputs = document.getElementsByTagName('input');
const labels = document.getElementsByTagName('label');
const select = document.getElementsByTagName('select');
const textarea = document.getElementById('id_roomproblemreason')
const countrySelect = document.getElementById('countrySelect')
const passaport = document.getElementById('passaport')

if(countrySelect){
    const country = async () => {
        try {
            const request = await fetch('https://restcountries.com/v3.1/all')
            const response = await request.json()
            console.log(response);
            response.forEach(country => {
                let optionCountry = document.createElement("option");
                optionCountry.value = country.cca2;
                optionCountry.textContent = country.cca2;
                countrySelect.appendChild(optionCountry)
            })
        } catch (error) {
            console.log("apiden gelen hata", error);
        }
    }
    country()
}


textarea.classList.add('form-control', 'mb-3')
textarea.rows = 5

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
            inputs[j].classList.add('form-check-input', 'ms-2');

            // İlgili label ile inputu bir araya getir
            if (label.htmlFor === inputs[j].id) {
                label.parentElement.insertBefore(inputs[j], label.nextSibling);
            }
        }
        else if (inputs[j].type == 'date') {
            inputs[j].classList.add('form-control')
            if (label.htmlFor === inputs[j].id) {
                label.parentElement.insertBefore(inputs[j], label.nextSibling)
            }
        }
    }
    for (let k = 0; k < select.length; k++) {
        select[k].classList.add('form-select')
        if (label.htmlFor == select[k].id) {
            label.parentElement.insertBefore(select[k], label.nextSibling)
        }
    }
}

// Reuqired Ver
countrySelect.onchange = function(e){
    if(e.target.value !== "TR"){
        passaport.setAttribute('required','')
    }else {
        passaport.removeAttribute('required')
    }
}