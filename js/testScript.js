function buttonOneEntered(event) {
  // add button emphasis
  event.currentTarget.classList.add("buttonEmphasize");

  // remove styles for button two
  const buttonBackground = document.querySelector(".buttonBackground");
  if (buttonBackground) {
    buttonBackground.classList.remove("buttonTwoBackground");
    buttonBackground.classList.add("buttonOneBackground");
  }
}

function buttonOneExited(event) {
  event.currentTarget.classList.remove("buttonEmphasize");
  const buttonBackground = document.querySelector(".buttonBackground");
  if (buttonBackground) {
    buttonBackground.classList.remove("buttonOneBackground");
    buttonBackground.classList.remove("buttonTwoBackground");
  }
}

function buttonTwoEntered(event) {
  // add button emphasis
  event.currentTarget.classList.add("buttonEmphasize");

  const buttonBackground = document.querySelector(".buttonBackground");
  if (buttonBackground) {
    buttonBackground.classList.remove("buttonOneBackground");
    buttonBackground.classList.add("buttonTwoBackground");
  }
}

function buttonTwoExited(event) {
  event.currentTarget.classList.remove("buttonEmphasize");
  const buttonBackground = document.querySelector(".buttonBackground");
  if (buttonBackground) {
    buttonBackground.classList.remove("buttonOneBackground");
    buttonBackground.classList.remove("buttonTwoBackground");
  }
}