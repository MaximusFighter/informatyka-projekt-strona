function checkInput() {
  var inputElement = document.getElementById('inputText');
  var resultElement = document.getElementById('result');

  if (inputElement.value.toUpperCase() === 'KONSOLA') {
    resultElement.innerText = 'Dobrze';
    resultElement.style.color = 'green';
  } else {
    resultElement.innerText = 'Źle';
    resultElement.style.color = 'red';
  }
}

function showHints() {
  document.getElementById("wskazowka").innerHTML = "<b>(kontener - tener) + (solarium - rium))</b>"
}