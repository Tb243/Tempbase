import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};

export default class ProcessAndMeasureTempScreen extends React.Component<TProps> {
	render() {
		return (
			<div className="screenProcessAndMeasureTemp">
				<p>This is the process and measure temperature screen and will display a loading icon</p>
			</div>
		);
	}
}