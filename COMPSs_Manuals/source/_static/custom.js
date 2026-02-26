// PARTICLES

document.addEventListener("DOMContentLoaded", () => {
  const today = new Date();
  const month = today.getMonth() + 1;
  const day = today.getDate();

  function createParticle(symbol) {
    const particle = document.createElement("span");
    particle.className = "particle";
    particle.style.left = Math.random() * 100 + "vw"; // random horizontal position
    particle.style.fontSize = (Math.random() * 20 + 12) + "px"; // random size
    particle.style.animationDuration = (Math.random() * 3 + 3) + "s"; // random speed
    particle.innerText = symbol;
    document.body.appendChild(particle);

    // Remove DOM when the animation finishes
    particle.addEventListener("animationend", () => particle.remove());
  }

  // Christmas: 24-25 december
  if ((month === 12 && day === 24) || (month === 12 && day === 25)) {
    const interval = setInterval(() => createParticle("❄️"), 300); // every 0.3s
  }

  // Sant Jordi: 23 april
  if (month === 4 && day === 23) {
    const interval = setInterval(() => createParticle("🌹"), 400); // every 0.4s
  }

  // Activate roses with Ctrl + Alt + R
  document.addEventListener("keydown", (e) => {
    if (e.ctrlKey && e.altKey && e.key.toLowerCase() === "r") {
      const interval = setInterval(() => createParticle("🌹"), 300);
      // Stop after 5 seconds
      setTimeout(() => clearInterval(interval), 5000);
    }
  });
});

// Activación con Ctrl + Alt + G
//document.addEventListener("keydown", (e) => {
//  if (e.ctrlKey && e.altKey && e.key.toLowerCase() === "g") {
//    alert("🎮 ¡Bienvenido al juego paralelo COMPSs! (demo placeholder)");
//    // Aquí podrías inicializar un canvas o mini juego real
//  }
//});