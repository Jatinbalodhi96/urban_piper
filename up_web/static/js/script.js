$(document).ready(app)

var ws;


function app () {
    console.log('app init')
    var url = 'ws://' + window.location.host + '/connect';
    
    ws = new WebSocket(url)
    ws.addEventListener('open', function(event) {
        console.log('connected to websocket')
        // render all tasks list
    })
    
    $('#create_task').on('click', create_task)
}


function create_task() {
    var task_data = {
        'title': $('input[name=title]').val(),
        'priority': $('input[name=priority]').val(),
        'created_by': $('input[name=username]').val()
    }

    if (task_data.title !== "") {
        ws.send(JSON.stringify(task_data))
    }
}