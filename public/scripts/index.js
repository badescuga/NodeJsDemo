
var socket;
start();

function start() {
	socket = io.connect();
	socket.on('connect', (data) => {

	});

	socket.on('reconnect', (data) => {
		var name = $('#currentStatus').text('');
		if (name && name.length > 0) {
			login();
		}
	});

	socket.on('disconnect', (data) => {
		$('#currentStatus').text('Disconnected from server; Trying to reconnect');
	});

	//handling video stream

	socket.on("videoStream", function (data) {
	 $("#videoStream").attr('src','data:image/jpeg;base64, ' + data);
	});

}

function login() {
	var name = $('#userName').val();
	console.log(` >>> web client >>> ${name}`);

	//login
	socket.emit('login', {
		'connectedType': 'controller',
		'name': name
	}, (data) => {
		console.log(' >>> web client >>> login >>> received login back');
		$('#currentStatus').text('Connected!');
	});
};

//function for moving the robot
function move(direction) {
	console.log(` >>> web client >>> move ${direction}`);
	socket.emit('moveRobot',
		{ 'direction': direction },
		(data) => {
			console.log(` >>> web client >>> response move robot ${data}`);
		});
}

function startStream() {

	socket.emit('startClientVideoStream', null, (data) => {
	console.log(' >>> web client >>> start video stream');
	});
}

function stopStream() {
	console.log(' >>> web client >>> stop video stream');
	socket.emit('stopClientVideoStream', null, (data) => {
	console.log(' >>> web client >>> stop video stream');
	});
}