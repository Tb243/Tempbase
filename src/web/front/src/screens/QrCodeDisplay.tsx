import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};
//data value in this function needs to be changed
export default class QrCodeDisplayScreen extends React.Component<TProps> {
	render() {
		return (
			<div className="screenQrCodeDisplay">
				<p>This is the QR code display screen and this is where the QR code goes</p>
				<p>Your temperature is {this.props.data.temperatureMeasurement}</p>
			</div>
		);
	}
}