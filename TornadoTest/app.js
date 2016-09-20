$(document).ready(function () {
			var ws = new WebSocket('http://localhost:8896/server');

			ws.onopen = function (evt) {
				var conn_status = document.getElementById('conn_text');
				conn_status.innerHTML = "Connection status: Connected!";
			};

			ws.onmessage = function (evt) {
				var newMessage = document.createElement('p');
				newMessage.textContent = "Server: " + evt.data;
				document.getElementById('messages_txt').appendChild(newMessage);
			};

			ws.onclose = function(evt) {
				alert ("Connection closed");
			};

			$('.button').on('click', function (evt) {
				evt.prevetDefault();
				var newMessage = document.cleateElement('p');
				newMessage.textContent = "Client: " + message;
				var message = $('.input_text').val();
				ws.send(message);

				document.getElementById('messages_txt').appendChild(newMessage);
			});
		});
