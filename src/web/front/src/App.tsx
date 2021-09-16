import React from 'react';

// Import your screens here.
import StateSetupScreen from "./screens/StateSetupScreen";

import './App.css';

type TProps = {};
type TState = {
	screen: TTempBaseScreens;
	data: TTempBaseFsmData;
};

const DEBUG = true;

class App extends React.Component<TProps, TState> {
	private socket?: WebSocket;

	constructor(props: TProps) {
		super(props);

		this.state = {
			screen: "setup",
			data: {}
		};
	}

	getScreen() {
		switch (this.state.screen) {
			case "setup":
				return <StateSetupScreen data={this.state.data} />

			// Add your screens here.

		}

		return (
			<p>No "{this.state.screen}" screen is connected!</p>
		);
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
			<div className="app">
				<div className="screen">
					{this.getScreen()}
				</div>

				{DEBUG ? (
					<footer>
						<pre>Screen: {this.state.screen}</pre>
						<pre>FSM Data:</pre>
						<pre>{JSON.stringify(this.state.data, null, 4)}</pre>
					</footer>
				) : null}
			</div>
		);
	}
}

export default App;
