function addItem() {
    let text_input = document.getElementById('newItemText').value
    let new_li = document.createElement('li')

    let ul_to_attach_that_new_li_bro = document.getElementById('items')
    ul_to_attach_that_new_li_bro.appendChild(new_li).textContent = text_input

    document.getElementById('newItemText').value = ''
    print('working')
}

// <label for="newItemText"></label><input type="text" id="newItemText" >
//                 <input type="button" value="Add" onclick="addItem()">


//                 <script>
//                      let user = document.getElementById('user').innerText = ''
//                     function addItem() {
//                     let text_input = document.getElementById('newItemText').value
//                     let new_li = document.createElement('li')
//
//                     let ul_to_attach_that_new_li_bro = document.getElementById('items')
//                     ul_to_attach_that_new_li_bro.appendChild(new_li).textContent = text_input
//
//                     document.getElementById('newItemText').value = ''
//
// }
//                 </script>
