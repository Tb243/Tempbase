import React from 'react';
import './App.css';

type TProps = {};
type TState = {
	screen: "setup" | "waitForHand" | "rejectUser" | "processAndStoreTemperature" | "measureTemperature" | "displayQrCode" | "dispenseSanitiser";
};

class App extends React.Component<TProps, TState> {

	constructor(props: TProps) {
		super(props);

		this.state = {
			screen: "setup"
		};
	}

	componentDidMount() {

	}

	render() {
		return (
			<div className="App">
				<header className="App-header">
					<p>
						The current FSM state is <code>{this.state.screen}</code>
					</p>
				</header>
			</div>
		);
	}
}

export default App;
