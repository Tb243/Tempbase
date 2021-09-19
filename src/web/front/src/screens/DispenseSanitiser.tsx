import React from "react";

type TProps = {
	data: TTempBaseFsmData;
};

export default class DispenseSanitiserScreen extends React.Component<TProps> {
	render() {
		return (
			<div className="screenDispenseSanitiser">
				<p>Dispensing sanitiser...</p>
				<img src="sanitiser.png" alt="hands image"></img>
			</div>
		);
	}
}