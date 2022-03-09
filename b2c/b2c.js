// Create WebSocket connection.
const socket = new WebSocket('ws://82.6.205.72:7790');

// Connection opened
socket.addEventListener('open', function (event) {
    socket.send('Hello Server!');
});

// Listen for messages
socket.addEventListener('message', function (event) {
    console.log('Message from server ', event.data);
    let v = document.getElementById('results').innerHTML;
    v = event.data + "<br> "+ v;
    document.getElementById('results').innerHTML = v;
});

function sendChat(){
    let v = document.getElementById('fname').value;

    console.log(v);
    socket.send(v);
} 