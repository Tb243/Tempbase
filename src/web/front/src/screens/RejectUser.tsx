import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};

export default class RejectUserScreen extends React.Component<TProps> {
	render() {
		return (
			<div className="screenRejectUser">
				<p>Warning: elevated temperature!</p>
				<p>Your temperature is {this.props.data.temperatureMeasurement?.toFixed(1)}</p>
				<div><img src="cross.png" alt="black x image"></img></div> 
				<p>Please measure your temperature again...</p>
			</div>
		);
	}
}