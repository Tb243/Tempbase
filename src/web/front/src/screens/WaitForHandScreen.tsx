import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};

export default class WaitForHandScreen extends React.Component<TProps> {
	render() {
		return (
			<div className="screenWaitForHand">
				<p>Welcome, please stand on the yellow line. <br></br> Place your hand under the dispenser…</p>
				<img src="logo192.png" alt="TempBase Logo"></img>
			</div>
		);
	}
}