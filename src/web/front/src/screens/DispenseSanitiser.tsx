import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};

export default class DispenseSanitiserScreen extends React.Component<TProps> {
	render() {
		return (
			<div className="screenDispenseSanitiser">
				<p>This is the dispense sanitiser screen</p>
			</div>
		);
	}
}