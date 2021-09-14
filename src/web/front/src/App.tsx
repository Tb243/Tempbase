import React from 'react';
import './App.css';

type TProps = {};
type TState = {
	screen: "setup" | "waitForHand" | "rejectUser" | "processAndStoreTemperature" | "measureTemperature" | "displayQrCode" | "dispenseSanitiser";
	data: any;
};

class App extends React.Component<TProps, TState> {
	private socket?: WebSocket;

	constructor(props: TProps) {
		super(props);

		this.state = {
			screen: "setup",
			data: {}
		};
	}

	public componentDidMount() {
		this.tryConnectWebSocket();
	}

	public tryConnectWebSocket() {
		if (this.socket)
			return;

		this.socket = new WebSocket("ws://localhost:8080");

		this.socket.addEventListener("open", (event) => {
			console.log("Connection to WebSocket server opened.");
		});

		this.socket.onerror = (ev: Event) => {
			console.log("WebSocket Error!");
			this.socket?.close();
		};

		// If the FSM stops for some reason, try to reconnect.
		this.socket.addEventListener("close", (event) => {
			console.log("Connection to WebSocket lost!");
			this.socket = undefined;
			window.setTimeout(this.tryConnectWebSocket.bind(this), 500);
		});

		this.socket.addEventListener("message", (event) => {
			try {
				const data = JSON.parse(event.data);
				this.setState({
					...this.state,
					screen: data.state,
					data: data.stateData
				});
			} catch (e) {
				console.log("Malformed data received from WSS");
				console.log(e);
			}
		});
	}

	public render() {
		return (
			<div className="App">
				<header className="App-header">
					<p>
						The current FSM state is <code>{this.state.screen}</code>
					</p>
					<p>FSM State Data</p>
					<code>{Object.keys(this.state.data).length > 0 ? JSON.stringify(this.state.data, null, 4) : ""}</code>
				</header>
			</div>
		);
	}
}

export default App;
