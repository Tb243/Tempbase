type TTempBaseScreens = "setup" | "waitForHand" | "rejectUser" | "processAndStoreTemperature" | "measureTemperature" | "displayQrCode" | "dispenseSanitiser";

type TTempBaseFsmData = {
	ultrasonicDistance?: number;
};