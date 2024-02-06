function checkInput() {
  var inputElement = document.getElementById('inputText');
  var resultElement = document.getElementById('result');

  if (inputElement.value.toUpperCase() === 'IP') {
    resultElement.innerText = 'Dobrze';
    resultElement.style.color = 'green';
  } else {
    resultElement.innerText = 'Źle';
    resultElement.style.color = 'red';
  }
}

function showHints() {
  document.getElementById("wskazowka").innerHTML = "<b>(iglo - glo) + (pilot - ilot)</b>"
}