import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};

export default class RejectUserScreen extends React.Component<TProps> {

	renderFirstScreen() {
		return (
			<div className="screenRejectUser">
				<p>Warning: elevated temperature!</p>
				<p className='p1'>Your temperature is {this.props.data.temperatureMeasurement?.toFixed(1)}</p>
				<img src="cross.png" alt="black x image"></img>
				<p className='p2'>Please measure your temperature again...</p>
			</div>
		);
	}

	renderSecondScreen() {
		return (
			<div className="screenRejectUser">
				<p>Warning: elevated temperature (second screen)!</p>
				<p className='p1'>Your temperature is {this.props.data.temperatureMeasurement?.toFixed(1)}</p>
				<img src="cross.png" alt="black x image"></img>
				<p className='p2'>Please measure your temperature again...</p>
			</div>
		);
	}

	render() {
		if (this.props.data.attemptCounter! < 2)
			return this.renderFirstScreen()
		else
			return this.renderSecondScreen()
	}
}