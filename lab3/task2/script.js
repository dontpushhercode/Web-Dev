const cat = document.getElementById('cat'); //cat emoji on header
const addBtn = document.getElementById('add_btn'); //add button
const todoInput = document.getElementById('todo_input'); //todo input field
const todoList = document.getElementById('todo_list_content'); //todo list div  

//cat emoji logic
cat.addEventListener('mouseenter', () => {
    cat.textContent = '≽(-⩊ -マ≼';
});

cat.addEventListener('mouseleave', () => {
    cat.textContent='≽(•⩊ •マ≼';
});

//main logic
addBtn.addEventListener('click', ()=> {
    const text = todoInput.value.trim();
    if(text!=""){
        const todoItem = document.createElement('div');
        todoItem.classList.add('todo_item');
        
        const checkBox = document.createElement('input');
        checkBox.type = 'checkbox';
        checkBox.id = "checkbox"+Date.now();

        const label = document.createElement('label');
        label.textContent = text;

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = '×';
        deleteBtn.classList.add('delete_btn');

        deleteBtn.addEventListener('click', () => { //remover
            todoItem.remove();
        });

        todoItem.appendChild(checkBox);
        todoItem.appendChild(label);
        todoItem.appendChild(deleteBtn);

        todoList.prepend(todoItem); 

        todoInput.value = '';
    }
});

todoInput.addEventListener('input', () => {
    const maxLength = 50;
    if(todoInput.value.length > maxLength){
        todoInput.value = todoInput.value.slice(0, maxLength);
        alert("Максимум 50 символов!");
    }
});

