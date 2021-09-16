import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};

export default class WaitForHandScreen extends React.Component<TProps> {
	render() {
		return (
			<div className="screenWaitForHand">
				<p>This is the wait for hand screen and the distance to the users hand is {this.props.data.ultrasonicDistance}</p>
				{this.props.data.ultrasonicDistance! < 5 ? "It's less than 5" : "It's greater than or equal to five"}
			</div>
		);
	}
}