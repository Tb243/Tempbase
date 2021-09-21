import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};

export default class ProcessAndMeasureTempScreen extends React.Component<TProps> {
	render() {
		return (
			<div className="screenProcessAndMeasureTemp">
				<div><img src="loading.gif" alt="loading gif"></img></div> 
			</div>
		);
	}
}