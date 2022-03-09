// Create WebSocket connection.
const socket = new WebSocket('ws://82.6.205.72:7790');
let seen = [];
let users = {}
let my_id = null;

// Connection opened
socket.addEventListener('open', function (event) {
    //socket.send('Hello Server!');
});

function add_msg(text){
    let v = document.getElementById('results').innerHTML;
    let dt = new Date().toLocaleString();
    text = `[${dt}] ${text}`
    v = text + "<br> "+ v;
    document.getElementById('results').innerHTML = v;

}

function update_seen(){
    document.getElementById('users').innerHTML = seen.join("<br>");
}

function removeItemOnce(arr, value) {
    var index = arr.indexOf(value);
    if (index > -1) {
      arr.splice(index, 1);
    }
    return arr;
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
    } else if(evt == "ID"){
        my_id = event.data.split("/")[2];
        console.log(`ID defined ${my_id}`)
    } else if(evt == "TEST"){
        seen.push(event.data.split("/")[3]);
        update_seen();
        users[event.data.split("/")[2]] = event.data.split("/")[3];
        add_msg(`${event.data.split("/")[3]} joined the chat.`)
    } else if(evt == "DISCONNECT"){
        add_msg(`${users[event.data.split("/")[2]]} left the chat.`)
        removeItemOnce(seen, users[event.data.split("/")[2]]);
        users[event.data.split("/")[2]] = null;
        //add_msg(`${}`)
        
        update_seen()
    } else {
        let line = event.data.split("/")[2];
        console.log(evt+" "+line);
    }

});

window.onload = function() {
    document.getElementById('ftext').disabled = true;
    document.getElementById('ftext').addEventListener('keyup',function(e){
        if (e.keyCode === 13) {
            sendChat();
      }
    });
}

function doConnect(){
    let name = document.getElementById('fname').value;
    if(name == ""){
        add_msg("Name is needed...");
        return
    }
    console.log(my_id);
    console.log(name);
    socket.send("/TEST/"+my_id+"/"+name+"/");
    document.getElementById('fname').disabled = true;
    document.getElementById('ftext').disabled = false;
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