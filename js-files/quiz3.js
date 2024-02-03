let selectedAnswers = [];

function selectAnswer(element, answer, questionNumber) {
  if (selectedAnswers.find(item => item.questionNumber === questionNumber)) {
    return;
  }

  selectedAnswers = selectedAnswers.filter(item => item.questionNumber !== questionNumber);

  element.classList.add('selected');
  selectedAnswers.push({ element, answer, questionNumber });
}

function showResult() {
  let resultContainer = document.getElementById('result');
  let correctAnswers = 0;

  selectedAnswers.forEach(item => {
    const isCorrect = checkAnswer(item.answer, item.questionNumber);
    if (isCorrect) {
      item.element.classList.add('correct');
      correctAnswers++;
    } else {
      item.element.classList.add('incorrect');
      const correctElement = document.querySelector(`.answer[data-answer="${checkCorrectAnswer(item.questionNumber)}"][data-question="${item.questionNumber}"]`);
      if (correctElement) {
        correctElement.classList.add('correct');
      }
    }
  });

  resultContainer.innerHTML = `Liczba poprawnych odpowiedzi: ${correctAnswers}`;
}

function checkAnswer(answer, questionNumber) {
  return answer === checkCorrectAnswer(questionNumber);
}

function checkCorrectAnswer(questionNumber) {
  switch (questionNumber) {
    case 1:
      return 'B';
    case 2:
      return 'C';
    case 3:
      return 'A';
    case 4:
      return 'D';
    case 5:
      return 'A';
    case 6:
      return 'C';
    case 7:
      return 'A';
    case 8:
      return 'D';
    case 9:
      return 'B';
    case 10:
      return 'C';
    default:
      return '';
  }
}

function resetQuiz() {
  selectedAnswers.forEach(item => {
    item.element.classList.remove('selected', 'correct', 'incorrect');
  });

  selectedAnswers = [];
  document.getElementById('result').innerHTML = '';
}

