function calculaAreaRetangulo(largura, altura) {
    
    if (typeof largura === 'number' && typeof altura === 'number' && largura > 0 && altura > 0) {
      
        const area = largura * altura;
        return area;
    } else {
       
        return "Parâmetros inválidos. Certifique-se de que largura e altura sejam números positivos.";
    }
}


const retanguloForm = document.getElementById('retangulo-form');
const larguraInput = document.getElementById('largura');
const alturaInput = document.getElementById('altura');
const resultadoElement = document.getElementById('resultado');


document.getElementById('calcular').addEventListener('click', function () {
    const largura = parseFloat(larguraInput.value);
    const altura = parseFloat(alturaInput.value);

    const area = calculaAreaRetangulo(largura, altura);
    resultadoElement.textContent = `A área do retângulo é ${area}`;
});
