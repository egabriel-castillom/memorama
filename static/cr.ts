let tiempoRestante: number = Number(localStorage.getItem('tiempoRestante')) || 60; // 60 segundos
const elementoCuentaRegresiva: HTMLElement | null = document.getElementById('cuenta-regresiva');

const startCounterElement = document.getElementById('startCounter') as HTMLInputElement;
const startCounter = startCounterElement ? parseInt(startCounterElement.value) : 0;

const actualizarCuentaRegresiva = (): void => {
  if (startCounter === 1) {
    tiempoRestante = 60;
  }
  if (elementoCuentaRegresiva) {
    elementoCuentaRegresiva.textContent = `${tiempoRestante} segundos restantes`;
  }
  tiempoRestante -= 1;
  if (tiempoRestante === 0) {
    tiempoRestante = 60;
  }
  localStorage.setItem('tiempoRestante', tiempoRestante.toString());
  if (tiempoRestante >= 0) {
    setTimeout(actualizarCuentaRegresiva, 1000);
  }
};

actualizarCuentaRegresiva();