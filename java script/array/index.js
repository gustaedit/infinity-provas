
       
        function encontrarValorMaximo(lista) {
            const numeros = lista.split(',').map(Number);

            if (numeros.length === 0) {
                return undefined; 
            }

            return Math.max(...numeros); 
        }

       
        function encontrarValorMinimo(lista) {
            const numeros = lista.split(',').map(Number); 

            if (numeros.length === 0) {
                return undefined; 
            }

            return Math.min(...numeros); 
        }

       
        const numerosForm = document.getElementById('numeros-form');
        const numerosInput = document.getElementById('numeros');
        const resultadoElement = document.getElementById('resultado');

     
        document.getElementById('calcular').addEventListener('click', function () {
            const listaNumeros = numerosInput.value;

            const maximo = encontrarValorMaximo(listaNumeros);
            const minimo = encontrarValorMinimo(listaNumeros);

            if (maximo !== undefined && minimo !== undefined) {
                resultadoElement.textContent = `Valor Máximo: ${maximo}, Valor Mínimo: ${minimo}`;
            } else {
                resultadoElement.textContent = "Insira uma lista válida de números.";
            }
        });
