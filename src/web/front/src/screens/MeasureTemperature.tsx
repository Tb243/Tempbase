import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};

export default class MeasureTemperatureScreen extends React.Component<TProps> {
	render() {
		return (
			<div className="screenMeasureTemperature">
				<p>Measuring your temperature...</p>
				<img src="temp.png" alt="thermometer"></img>
			</div>
		);
	}
}