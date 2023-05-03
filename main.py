tasks = []

def add_task():
    text_input = Element("input")
    text_value = text_input.element.value
    if text_value == "":
        list_updated()
    else:
        same_task = False
        i = 0
        for task in tasks:
            if task == text_value:
                same_task = True
                tasks.pop(i)
            i += 1
        if same_task == False:
            tasks.append(text_value)
        text_input.element.value = ""
        #print(tasks)
        list_updated()

def enter_task(txt_input):
    if txt_input.key == "Enter":
        add_task()

Element("input").element.onkeypress = enter_task

def list_updated():
    item_list_html = ""
    if len(tasks) == 0:
        item_list_html = "<h5>No Tasks are set</h5>"
    else:
        for i in range(len(tasks)):
            item_list_html += f"<h5>• {tasks[i]}</h5>"
    item_list = Element("item_list")
    item_list.element.innerHTML = item_list_html
