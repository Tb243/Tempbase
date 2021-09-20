import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};

export default class RejectUserScreen extends React.Component<TProps> {
	render() {
		return (
			<div className="screenRejectUser">
				<p>Warning: elevated temperature!</p>
				<p className='p1'>Your temperature is {this.props.data.temperatureMeasurement?.toFixed(1)}</p>
				<img src="cross.png" alt="black x image"></img>
				<p className='p2'>Please measure your temperature again...</p>
			</div>
		);
	}
}