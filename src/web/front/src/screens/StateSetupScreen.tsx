import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};

export default class StateSetup extends React.Component<TProps> {
	render() {
		return (
			<div className="screenSetup">
				<p>Welcome to TempBase - the all in one check-in station. <br></br> TempBase is loading...</p>
				<div><img src="loading.gif" alt="loading gif"></img></div> 
			</div>
		);
	}
}