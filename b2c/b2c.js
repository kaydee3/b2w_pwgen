// Create WebSocket connection.
const socket = new WebSocket('ws://82.6.205.72:7790');
let seen = [];

// Connection opened
socket.addEventListener('open', function (event) {
    //socket.send('Hello Server!');
});

function add_msg(text){
    let v = document.getElementById('results').innerHTML;
    v = text + "<br> "+ v;
    document.getElementById('results').innerHTML = v;
}

function update_seen(){
    document.getElementById('users').innerHTML = seen.join("<br>");
}

// Listen for messages
socket.addEventListener('message', function (event) {
    console.log('Message from server ', event.data);
    let evt = event.data.split("/")[1];
    
    if(evt == "MSG"){
        let sender = event.data.split("/")[2];
        let line = event.data.split("/")[3];
        add_msg(`${sender}: ${line}`);
        if(!seen.includes(sender)) seen.push(sender);
        update_seen();
    } else {
        let line = event.data.split("/")[2];
        add_msg(evt+" "+line)
    }

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
    socket.send("/MSG/"+name+"/"+v+"/");
    document.getElementById('ftext').value = "";
} 