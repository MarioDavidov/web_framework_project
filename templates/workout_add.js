function addItem() {
    let text_input = document.getElementById('newItemText').value
    let new_li = document.createElement('li')

    let ul_to_attach_that_new_li_bro = document.getElementById('items')
    ul_to_attach_that_new_li_bro.appendChild(new_li).textContent = text_input

    document.getElementById('newItemText').value = ''
    print('working')
}