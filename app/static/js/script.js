document.getElementById("form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const ciudad = document.getElementById("ciudad").value;
    const resultado = document.getElementById("resultado");

    resultado.innerHTML = "⏳ Buscando clima...";

    try {
        const res = await fetch(`/categorias/${ciudad}`);
        const data = await res.json();

        if (data.error) {
            resultado.innerHTML = `<p style="color:red">${data.error}</p>`;
        } else {
            resultado.innerHTML = `
                <h2>${data.ciudad}</h2>
                <p>🌡️ Temperatura: ${data.temperatura} °C</p>
                <p>💧 Humedad: ${data.humedad}%</p>
                <p>📊 Presión: ${data.presion} hPa</p>
                <p>📝 Descripción: ${data.descripcion}</p>
            `;
        }
    } catch (err) {
        resultado.innerHTML = `<p style="color:red">Error al obtener los datos</p>`;
    }
});
