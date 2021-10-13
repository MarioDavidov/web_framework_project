function calculate() {

    let age = document.getElementById('age').value
    let height = document.getElementById('height').value
    let weight = document.getElementById('weight').value
    let genderM = document.getElementById('male').value
    let genderF = document.getElementById('female').value
    const rbs = document.querySelectorAll('input[name="gender"]');
  console.log('workss 1113')
    // if (Number.isInteger(age) && Number.isInteger(height) && Number.isInteger(weight)){
        console.log('workss')
    let selectedValue;
    for (const rb of rbs) {
        if (rb.checked) {
            selectedValue = rb.value;
            break;
        }
    }
    // Men: BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) - (5.677 x age in years)
    // Women: BMR = 447.593 + (9.247 x weight in kg) + (3.098 x height in cm) - (4.330 x age in years)

    function calc(selectedValue){
        let mresult = 0
        let fresult = 0
        console.log(selectedValue)
        if (selectedValue === "male"){
            mresult += 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
            return mresult
        }
        if (selectedValue === "female") {
            fresult += 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
            return fresult
        }
    }
    document.getElementById('age').value = ''
    document.getElementById('height').value = ''
    document.getElementById('weight').value = ''
    // document.getElementById('male').value = ''
    // document.getElementById('female').value = ''
    console.log((Math.round(calc(selectedValue))))
    let result = (Math.round(calc(selectedValue)))
    if(!isNaN(result)) {
        document.getElementById('result').innerHTML = result
        document.getElementById('first-int').innerText = Math.round(result * 1.2)
        document.getElementById('second-int').innerText = Math.round(result * 1.4)
        document.getElementById('third-int').innerText = Math.round(result * 1.45)
        document.getElementById('four-int').innerText = Math.round(result * 1.55)
        document.getElementById('five-int').innerText = Math.round(result * 1.7)
        document.getElementById('six-int').innerText = Math.round(result * 1.9)
    }
 // }
}