// PARTICLES (multiplatform)

document.addEventListener("DOMContentLoaded", () => {
  const today = new Date();
  const month = today.getMonth() + 1;
  const day = today.getDate();

  function createParticle(symbol) {
    const particle = document.createElement("span");
    particle.className = "particle";
    particle.style.left = Math.random() * 100 + "vw";
    particle.style.fontSize = (Math.random() * 20 + 12) + "px";
    particle.style.animationDuration = (Math.random() * 3 + 3) + "s";
    particle.innerText = symbol;
    document.body.appendChild(particle);
    particle.addEventListener("animationend", () => particle.remove());
  }

  // Christmas: 24-25 december
  if ((month === 12 && day === 24) || (month === 12 && day === 25)) {
    setInterval(() => createParticle("❄️"), 300);
  }

  // Sant Jordi: 23 april
  if (month === 4 && day === 23) {
    setInterval(() => createParticle("🌹"), 400);
  }

  // Detect if Mac
  let isMac = false;
  if (navigator.userAgentData) {
    isMac = navigator.userAgentData.platform === "Mac OS X";
  } else {
    isMac = /Mac/.test(navigator.userAgent);
  }

  // Activate Roses with Ctrl/Cmd + Alt/Option + R
  document.addEventListener("keydown", (e) => {
    const key = e.key.toLowerCase();
    const pressedMac = isMac && e.metaKey && e.altKey && key === "r";
    const pressedWin = !isMac && e.ctrlKey && e.altKey && key === "r";

    if (pressedMac || pressedWin) {
      const interval = setInterval(() => createParticle("🌹"), 300);
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