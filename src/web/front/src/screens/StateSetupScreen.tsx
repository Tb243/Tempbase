import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};

export default class StateSetup extends React.Component<TProps> {
	render() {
		return (
			<div className="screenSetup">
				<p>Welcome! <br></br> TempBase is loading...</p>
				<img src="loading.gif" alt="loading gif"></img>
			</div>
		);
	}
}