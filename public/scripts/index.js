
var socket;

function login() {
	var name = $('#userName').val();
	console.log(` >>> web client >>> ${name}`);
	socket = io.connect();

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
	console.log(` >>> web client >>> move ${direction}`)
	socket.emit('moveRobot', 
	{ 'direction': direction },
	(data) => {
	console.log(` >>> web client >>> response move robot ${data}`);	
	});
}