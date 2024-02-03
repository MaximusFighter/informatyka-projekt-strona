document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("formularz").addEventListener("submit", function(event) {
    event.preventDefault();
    window.alert("Formularz przesłany! Prosimy teraz o zgłoszenie się do pani Katarzyny Woźnicy w sali A23");
  });
});