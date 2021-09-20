import React from "react";
import QRCode from "qrcode.react";

type TProps = {
	data: TTempBaseFsmData;
};
//data value in this function needs to be changed
export default class QrCodeDisplayScreen extends React.Component<TProps> {
	render() {
		return (
			<div className="screenQrCodeDisplay">
				<p>Success: Your temperature is {this.props.data.temperatureMeasurement?.toFixed(1)}</p>
				<p>Please check in:</p>
				<p>Thank you and have a lovely day!</p>
			</div>
		);
	}
}