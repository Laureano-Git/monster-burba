<script lang="ts">
    import { PUBLIC_WHATSAPP_PHONE, PUBLIC_API_URL } from '$env/static/public';
    export let data;
    const burger = data.burger;

    // Variables de seleccion
    let tamano = burger.permite_simple ? "Simple" : (burger.permite_doble ? "Doble" : "Triple");
    let conCheddar = true;
    let conSalsa = true;
    let gaseosa = true;
    let papas = true;
    let direction = "";
    let name_client = "";
    let description = "";
    //cantidad de combos
    let cantidad = 1;

    //para las verduras
    // Usamos .split(", ") para que busque la coma y separe las palabras
    let listaVerduras = burger.ingredientes_default.split(", ");
    // Esta variable guardará las que el usuario No quiere
    let verdurasSeleccionadas = [...listaVerduras];

    // Logica de precios reactiva
    $: preciobase=0;
    $: {
        if (tamano === "Simple") preciobase=parseFloat(burger.precio_simple);
        else if (tamano === "Doble") preciobase=parseFloat(burger.precio_doble);
        else if (tamano === "Triple") preciobase=parseFloat(burger.precio_triple);
    };

    // Calculo del precio total segun tamanio y cantidad
    $: precioTotal = preciobase * cantidad;
    // Construccion del mensaje (reactivo)

    $: mensajeVerduras = verdurasSeleccionadas.length > 0 ? verdurasSeleccionadas.join(", ") : "sin verduras";

    $: pedidoListo= direction.trim().length > 5 && name_client.trim().length > 2;

$: mensajeTexto = `*NUEVO PEDIDO* 🍔
        -----------------------
        *Producto:* ${burger.nombre} (${tamano})
        *Cheddar:* ${conCheddar ? "Si" : "No"}
        *Salsa Especial:* ${conSalsa ? "Si" : "No"}
        *Verduras:* ${mensajeVerduras}
        *Con Gaseosa:* ${gaseosa ? "Si" : "No"}
        *Papas:* Incluidas 🍟 ${papas ? "Si" : "No"}
        *Cantidad:* ${cantidad}
        -----------------------
        *Dirección:* ${direction || "Direccion no indicada"}
        *A nombre de:* ${name_client}
        *Descripcion:* ${description || "Sin descripcion"}
        -----------------------
        *Total:* $${precioTotal.toFixed(2)}
        -----------------------`;
    
    $: whatsappUrl = `https://wa.me/${PUBLIC_WHATSAPP_PHONE}?text=${encodeURIComponent(mensajeTexto)}`;
</script>

<div class="pedido-container">
    <h1>Personaliza tu {burger.nombre}</h1>
    <p class="nota-papas"> 🍟 Todas nuestras burgers incluyen papas.</p>

    <form on:submit|preventDefault>
        <section class="grupo">
            <h3>Tamaño de la burga</h3>
            <div class="Opciones-radio">
                {#if burger.permite_simple}
                    <label>
                        <input type="radio" bind:group={tamano} value="Simple">Simple
                        Simple (${burger.precio_simple})
                    </label>                    
                {/if}
                {#if burger.permite_doble}
                    <label>
                        <input type="radio" bind:group={tamano} value="Doble">Doble
                        Doble (${burger.precio_doble})
                    </label>        
                {/if}
                {#if burger.permite_triple}
                    <label>
                        <input type="radio" bind:group={tamano} value="Triple">Triple
                        Triple (${burger.precio_triple})
                    </label>   
                {/if}
            </div>
        </section>

        <section class="grupo">
            <h3>Que le ponemos dentro?</h3>
            <label>
                <input type="checkbox" bind:checked={conCheddar}> Mucho Cheddar 🧀
            </label>
            <label>
                <input type="checkbox" bind:checked={conSalsa}> Salsa de la casa 🦍
            </label>
        </section>

        <section class="grupo">
            <h3>Que verduras usamos?</h3>
            {#each listaVerduras as v}
                <label>
                    <input type="checkbox" bind:group={verdurasSeleccionadas} value="{v}"> {v}
                </label>
            {/each}
        </section>

        <section class="grupo">
            <h3>Papas sazonadas?</h3>
            <input type="checkbox" bind:checked={papas}> Si, por favor
        </section>

        <section class="grupo">
            <h3> Sumamos gaseosa?</h3>
            <label class="toggle">
                <input type="checkbox" bind:checked={gaseosa}> Si, por favor 🥤
            </label>
        </section>

        <section>
            <h3>Donde enviamos el pedido?</h3>
            <input type="text" bind:value={direction} placeholder="Ej: calle 7, entre 46 y 47 numero 385" class="input-direction">
            <h3>Quien lo recibe?</h3>
            <input type="text" bind:value={name_client} placeholder="Ej: Gaston" class="input-direction">
            <h3>Alguna descripcion adicional del domicilio? (Opcional)</h3>
            <input type="text" bind:value={description} placeholder="Ej: Porton blanco con rejas negras" class="input-direction">
        </section>
    </form>
    <!--Resumen en tiempo real del pedido-->
    <div class="resumen-visual">
        <hr>
        <p><strong>Tu pedido es:</strong> {burger.nombre} {tamano}</p>
        <p><strong>Extras:</strong> {mensajeVerduras}</p>
        <p class="precio_final">Total: ${precioTotal.toFixed(2)}</p>
        <p><strong>Su pedido sera enviado a:</strong> {direction}</p>
    </div>

    <div class="footer-pedido">
        {#if pedidoListo}
            <a href="{whatsappUrl}" class="btn-whatsapp">
                Enviar Pedido (${(parseFloat(burger.precio)*cantidad).toFixed(2)})
            </a>
        {:else}
            <button class="btn-disabled" disabled>
                falta completar dirección y nombre
            </button>           
        {/if}
    </div>
</div>

<style>
    .Opciones-radio{
        display: flex;
        gap: 15px;
        margin-bottom: 20px;
    }
    .pedido-container{
        color: white;
    }
    .precio_final{
        font-size: 1.5rem;
        color: #09ff00;
        font-weight: bold;
    }
    .footer-pedido{
        padding: 1rem 0;
        text-decoration: none;
    }
    .input-direction {
    width: 100%;
    padding: 12px;
    background-color: #1a1a1a;
    border: 2px solid #00CCFF; /* Azul neón */
    color: white;
    border-radius: 8px;
    font-size: 1rem;
    margin-top: 10px;
    outline: none;
    transition: box-shadow 0.3s ease;
}

.input-direction:focus {
    box-shadow: 0 0 10px #00CCFF;
    border-color: #39FF14; /* Cambia a verde neón al escribir */
}

/* Botón deshabilitado (cuando falta completar datos) */
.btn-disabled {
    width: 100%;
    padding: 15px;
    background: #333;
    color: #666;
    border: none;
    border-radius: 10px;
    cursor: not-allowed;
    font-weight: bold;
}

/* Botón activo (WhatsApp) */
.btn-whatsapp {
    display: block;
    width: 100%;
    padding: 15px;
    background: #25D366; /* Color oficial WhatsApp */
    color: black;
    text-align: center;
    text-decoration: none;
    border-radius: 10px;
    font-weight: bold;
    box-shadow: 0 0 10px rgba(37, 211, 102, 0.5);
    transition: transform 0.2s;
}

.btn-whatsapp:hover {
    transform: scale(1.02);
    box-shadow: 0 0 20px rgba(37, 211, 102, 0.8);
}
</style>