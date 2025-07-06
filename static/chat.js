const socket = io({
  transports: ["websocket"]
});

const chatBox = document.getElementById('chat-box');
const input = document.getElementById('msg-input');

function sendMessage() {
  const message = input.value.trim();
  if (message) {
    const data = {
      uid: UID,
      username: USER,
      text: message
    };
    socket.send(data);
    input.value = '';
  }
}

socket.on('message', function(data) {
  const msgDiv = document.createElement('div');
  msgDiv.classList.add('msg');

  if (data.uid === UID) {
    msgDiv.classList.add('me');
  } else {
    msgDiv.classList.add('other');
  }

  msgDiv.innerHTML = `<strong>${data.username}:</strong> ${data.text}`;
  chatBox.appendChild(msgDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
});
