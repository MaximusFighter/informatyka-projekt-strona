let selectedAnswers = [];

function selectAnswer(element, answer, questionNumber) {
  if (selectedAnswers.find(item => item.questionNumber === questionNumber)) {
    return;
  }

  selectedAnswers = selectedAnswers.filter(item => item.questionNumber !== questionNumber);

  element.classList.add('selected');
  selectedAnswers.push({ element, answer, questionNumber });
}

let quizChecked = false;

function showResult() {
  if (quizChecked) {
    return;
  }

  let resultContainer = document.getElementById('result');
  let correctAnswers = 0;

  selectedAnswers.forEach(item => {
    const isCorrect = checkAnswer(item.answer, item.questionNumber);
    const feedbackElement = document.createElement('div');

    if (isCorrect) {
      item.element.classList.add('correct');
      feedbackElement.textContent = `Dobrze! (Pytanie ${item.questionNumber})`;
      correctAnswers++;
    } else {
      item.element.classList.add('incorrect');
      const correctAnswer = checkCorrectAnswer(item.questionNumber);
      feedbackElement.textContent = `Źle! Prawidłowa odpowiedź to ${correctAnswer} (Pytanie ${item.questionNumber})`;
      const correctElement = document.querySelector(`.answer[data-answer="${correctAnswer}"][onclick^="selectAnswer"][data-question="${item.questionNumber}"]`);
      if (correctElement) {
        correctElement.classList.add('correct');
      }
    }

    feedbackElement.classList.add(isCorrect ? 'correct' : 'incorrect');
    resultContainer.appendChild(feedbackElement);
  });

  resultContainer.innerHTML += `<div>Liczba poprawnych odpowiedzi: ${correctAnswers}</div>`;
  quizChecked = true;
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
      return 'B';
    case 4:
      return 'D';
    case 5:
      return 'C';
    case 6:
      return 'A';
    case 7:
      return 'C';
    case 8:
      return 'C';
    case 9:
      return 'A';
    case 10:
      return 'B';
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
  quizChecked = false;
}

