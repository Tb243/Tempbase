import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};

export default class WaitForHandScreen extends React.Component<TProps> {
	render() {
		return (
			<div className="screenWaitForHand">
				<div><img src="logo192.png" alt="TempBase Logo" className="logo-wfh"></img></div> 
				<p>Welcome, please stand on the yellow line. <br></br> Place your hand under the dispenser…</p>
			</div>
		);
	}
}