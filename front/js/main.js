import { Welcome } from "./Welcome.js";

const welcomeHeader = document.querySelector(".register__header__welcome");
const welcome = new Welcome(welcomeHeader);

const { hours } = welcome.getTimeOfDay();

if (hours >= 17) {
  welcomeHeader.textContent = "Dobry wieczór!";
}
welcome.tester();
