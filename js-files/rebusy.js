function checkInput() {
  var inputElement = document.getElementById('inputText');
  var resultElement = document.getElementById('result');

  if (inputElement.value.toUpperCase() === 'KOMPUTER') {
    resultElement.innerText = 'Wygrana';
  } else {
    resultElement.innerText = 'Źle';
  }
}
