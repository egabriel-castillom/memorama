let tiempoRestante = 60; // 60 segundos
const elementoCuentaRegresiva = document.getElementById('cuenta-regresiva');

const actualizarCuentaRegresiva = () => {
  elementoCuentaRegresiva.textContent = `${tiempoRestante} segundos restantes`;
  tiempoRestante -= 1;
  if (tiempoRestante >= 0) {
    setTimeout(actualizarCuentaRegresiva, 1000);
  }
};

actualizarCuentaRegresiva();