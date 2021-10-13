function addItem() {
    document.getElementById('first').textContent = 'working'
    let text_input = document.getElementById('newItemText').value
    let new_li = document.createElement('li')

    let ul_to_attach_that_new_li_bro = document.getElementById('items')
    ul_to_attach_that_new_li_bro.appendChild(new_li).textContent = text_input

    document.getElementById('newItemText').value = ''

}

    // <ul id="items" >
    //     <button onclick="addItem()">Add exercise</button>
    //     <li>
    //         <input id="newItemText" >
    //     </li>
    // </ul>