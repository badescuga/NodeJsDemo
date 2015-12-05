/**
 * Socket.io handle for 
 */

class SocketIOHandler {

	constructor(server) {
		console.log(' >>> starting socketio handler...');
		this.io = require('socket.io')(server);
		
		//handle socket connections
		//this._DefineHandles();
		
		//create arrays for connected components (users & robots)
		this.users = {};
		this.devices = {};

	}

	_DefineHandles() {
		this.io.on('connection', (socket) => {

			//on login 
			socket.on('login', (data, callback) => {
				var error = null;
				var response = null;
				console.log('am primit login de la client. ' + JSON.stringify(data));


				callback(error, response);
			});

			//on disconnect
			socket.on('disconnect', () => {
				console.log('disconnected socket: ' + socket.id);
				delete this.users[socket.id];
				delete this.devices[socket.id];
			});

		});
	}

}

export {
SocketIOHandler
};