// THEME TOGGLE

const STORAGE_KEY = "compss-docs-theme";

const sunIconSvg = `<svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="currentColor"><path d="M440-760v-160h80v160h-80Zm266 110-55-55 112-115 56 57-113 113Zm54 210v-80h160v80H760ZM440-40v-160h80v160h-80ZM254-652 140-763l57-56 113 113-56 54Zm508 512L651-255l54-54 114 110-57 59ZM40-440v-80h160v80H40Zm157 300-56-57 112-112 29 27 29 28-114 114Zm113-170q-70-70-70-170t70-170q70-70 170-70t170 70q70 70 70 170t-70 170q-70 70-170 70t-170-70Zm283-57q47-47 47-113t-47-113q-47-47-113-47t-113 47q-47 47-47 113t47 113q47 47 113 47t113-47ZM480-480Z"/></svg>`;
const moonIconSvg = `<svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="currentColor"><path d="M480-120q-150 0-255-105T120-480q0-150 105-255t255-105q14 0 27.5 1t26.5 3q-41 29-65.5 75.5T444-660q0 90 63 153t153 63q55 0 101-24.5t75-65.5q2 13 3 26.5t1 27.5q0 150-105 255T480-120Zm0-80q88 0 158-48.5T740-375q-20 5-40 8t-40 3q-123 0-209.5-86.5T364-660q0-20 3-40t8-40q-78 32-126.5 102T200-480q0 116 82 198t198 82Zm-10-270Z"/></svg>`;

// Get the theme from local storage or from the OS preference.
function getPreferredTheme() {
  const storedTheme = window.localStorage.getItem(STORAGE_KEY);

  if (storedTheme === "light" || storedTheme === "dark") {
    return storedTheme;
  }

  return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

// Update the document theme and the button label.
function applyTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);

  document.querySelectorAll(".theme-toggle-button").forEach((button) => {
    const icon = button.querySelector(".theme-toggle-icon");
    const label = button.querySelector(".theme-toggle-label");
    const nextMode = theme === "dark" ? "light" : "dark";

    if (icon) {
      icon.innerHTML = theme === "dark" ? sunIconSvg : moonIconSvg;
    }

    if (label) {
      label.textContent = nextMode === "dark" ? "Dark mode" : "Light mode";
    }

    button.setAttribute("aria-label", `Switch to ${nextMode} mode`);
    button.setAttribute("title", `Switch to ${nextMode} mode`);
  });
}

// Toggle between light and dark and save the choice.
function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute("data-theme") || getPreferredTheme();
  const nextTheme = currentTheme === "dark" ? "light" : "dark";
  window.localStorage.setItem(STORAGE_KEY, nextTheme);
  applyTheme(nextTheme);
}

// Create one theme toggle button.
function createThemeToggleButton() {
  const button = document.createElement("button");
  button.type = "button";
  button.className = "theme-toggle-button";
  button.innerHTML = '<span class="theme-toggle-icon" aria-hidden="true"></span>';
  button.addEventListener("click", toggleTheme);
  return button;
}

// Mount the theme toggle below the search input.
function mountThemeToggle() {
  const sidebarSearch = document.querySelector(".wy-side-nav-search");

  if (!sidebarSearch || sidebarSearch.querySelector(".theme-toggle-wrapper")) {
    return;
  }

  const wrapper = document.createElement("div");
  wrapper.className = "theme-toggle-wrapper";
  wrapper.appendChild(createThemeToggleButton());
  sidebarSearch.appendChild(wrapper);
}

// Initialize the theme system.
function initThemeToggle() {
  mountThemeToggle();
  applyTheme(getPreferredTheme());

  const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
  mediaQuery.addEventListener("change", (event) => {
    if (!window.localStorage.getItem(STORAGE_KEY)) {
      applyTheme(event.matches ? "dark" : "light");
    }
  });
}

// PARTICLES (multiplatform)

document.addEventListener("DOMContentLoaded", () => {
  initThemeToggle();

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

  // Navidad: 24-25 december
  if ((month === 12 && day === 24) || (month === 12 && day === 25)) {
    setInterval(() => createParticle("❄️"), 300);
  }

  // Sant Jordi: 23 april
  if (month === 4 && day === 23) {
    setInterval(() => createParticle("🌹"), 400);
  }

  // Shortcut Ctrl+Alt+R o Ctrl+Option+R (Mac)
  document.addEventListener("keydown", (e) => {
    const key = e.key.toLowerCase();
    const isMac = /Mac/.test(navigator.userAgent);

    // Windows/Linux: Ctrl+Alt+R
    const winLinux = !isMac && e.ctrlKey && e.altKey && key === "r";
    // Mac: Ctrl+Option+R
    const mac = isMac && e.ctrlKey && e.altKey && key === "r";

    if (winLinux || mac) {
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
