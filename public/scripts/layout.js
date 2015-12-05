
console.log(' >>> web >>> init');
//var socket = io.connect("http://localhost:3000");
var socket = io.connect();

socket.emit('login', {'testBadescuga':'lol'}, (data) => {
	console.log(' >>> web client >>> login >>> received login back');
});