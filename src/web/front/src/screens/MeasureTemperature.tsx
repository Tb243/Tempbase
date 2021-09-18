import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};

export default class MeasureTemperatureScreen extends React.Component<TProps> {
	render() {
		return (
			<div className="screenMeasureTemperature">
				<p>This is the measure temperature screen</p>
			</div>
		);
	}
}