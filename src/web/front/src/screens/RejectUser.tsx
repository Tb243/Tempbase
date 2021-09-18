import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};

export default class RejectUserScreen extends React.Component<TProps> {
	render() {
		return (
			<div className="screenRejectUser">
				<p>This is the reject user screen</p>
				<p>Your temperature is {this.props.data.temperatureMeasurement}</p>
			</div>
		);
	}
}