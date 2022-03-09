// Create WebSocket connection.
const socket = new WebSocket('ws://82.6.205.72:7790');

// Connection opened
socket.addEventListener('open', function (event) {
    socket.send('Hello Server!');
});

function add_msg(text){
    let v = document.getElementById('results').innerHTML;
    v = text + "<br> "+ v;
    document.getElementById('results').innerHTML = v;
}
// Listen for messages
socket.addEventListener('message', function (event) {
    console.log('Message from server ', event.data);
    add_msg(event.data)
    
});

window.onload = function() {
    document.getElementById('ftext').addEventListener('keyup',function(e){
        if (e.keyCode === 13) {
        sendChat();
      }
    });
}


function sendChat(){
    let name = document.getElementById('fname').value;
    let v = document.getElementById('ftext').value;
    if(name == ""){
        add_msg("Name is needed...");
        return
    }
    if(v == ""){
        add_msg("Text is needed...");
        return
    }
    console.log(v);
    socket.send(name+": "+v);
    document.getElementById('ftext').value = "";
} 