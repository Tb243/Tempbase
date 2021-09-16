import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};

export default class StateSetup extends React.Component<TProps> {
	render() {
		return (
			<div className="screenSetup">
				<p>This is the setup screen</p>
			</div>
		);
	}
}