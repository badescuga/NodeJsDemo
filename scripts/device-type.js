
class DeviceBase {

	constructor(socket) {
		this.socket = socket;
	}

}

class Robot extends DeviceBase {

	constructor(socket, data) {
		console.log(` >>> Initializing Robot; data: ${JSON.stringify(data) }`)
		super(socket);
		this.data = data;
	}

	Move(direction, callback) {
		this.socket.emit('moveRobot',
			{
				'direction': direction
			},
			(data) => {
				callback(data);
			}
			);
	}
}

class Controller extends DeviceBase {

	constructor(socket, data) {
		console.log(` >>> Initializing Controller; data: ${JSON.stringify(data) }`)
		super(socket);
		this.data = data;
		this.videoStreamEnabled = false;
	}

	StartVideoStream() {
		this.videoStreamEnabled = true;
	}

	StopVideoStream() {
		this.videoStreamEnabled = false;
	}

	SendVideoStream(data) {
		this.socket.emit('videoStream', data, (info) => {
			console.log(' >>> web server >>> emitted video to client');
		});
	}
}

export {Robot, Controller};