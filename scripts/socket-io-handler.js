/**
 * Socket.io handle for
 */

import {Robot, Controller} from './device-type.js';

class SocketIOHandler {

	constructor(server) {
		console.log(' >>> starting socketio handler...');
		this.io = require('socket.io')(server);

		//handle socket connections
		this._DefineHandles();

		//create arrays for connected components (users & robots)
		this.controllers = {};
		this.robots = {};

	}

	_DefineHandles() {
		this.io.on('connection', (socket) => {
			console.log(' >>> client has connected --- ');

			//on login
			socket.on('login', (data, callback) => {
				var error = null;
				var response = null;
				console.log(' >>> login de la client. ' + JSON.stringify(data));
				switch (data.connectedType) {
					case 'controller':
						this.controllers[socket.id] = new Controller(socket, data);
						break;
					case 'robot':
						this.robots[socket.id] = new Robot(socket, data);
						break;
				}

				callback(error, response);
			});

			//on move robot
			socket.on('moveRobot', (data, callback) => {
				console.log(' >>> moveRobot de la client. ' + JSON.stringify(data));
				for (var key in this.robots) { // no check at this point, will have a select list of devices
					this.robots[key].Move(data.direction, (data) => {
						callback(data);
					});
				}

				callback('moved Robot');
			});

			//stream
			socket.on('startClientVideoStream', (data, callback) => {
				// fs.readFile(__dirname + '/images/image.jpg', function (err, buf) {
				// 	// it's possible to embed binary data
				// 	// within arbitrarily-complex objects
				// 	socket.emit('image', { image: true, buffer: buf.toString('base64') });
				// 	console.log('image file is initialized');
				//});
				if(this.controllers[socket.id]) {
					this.controllers[socket.id].StartVideoStream();
				}
			});

			socket.on('stopClientVideoStream', (data,callback) => {
				if(this.controllers[socket.id]) {
					this.controllers[socket.id].StopVideoStream();
				}
			});

			socket.on('receivedImageStreamFromPi', (data,callback) => {
				for(var key in this.controllers) {
					if(this.controllers[key].videoStreamEnabled) {
					this.controllers[key].SendVideoStream(data);
					}
				}
			});




			//on disconnect
			socket.on('disconnect', () => {
				console.log(' >>> disconnected socket: ' + socket.id);
				delete this.controllers[socket.id];
				delete this.robots[socket.id];
			});

		});
	}

}

export {
SocketIOHandler
};