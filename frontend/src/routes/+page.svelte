<script>
    export let data;
    // Creamos una variable reactiva para no escribir "data.info" todo el tiempo
    $: negocio = data.info && data.info.length > 0 ? data.info[0] : null;
</script>
<div class="contacto-container">
    <img src="src\lib\assets\WhatsApp Image 2025-11-15 at 12.29.31.jpeg" alt="Logo">
    <h1>Mounstrosamente ricas!!!</h1>

    {#if negocio}
            <div class="item destacado">
                <h3> 🏠 Zona de Atención </h3>
                <b><p>{negocio.zona_atencion}</p></b>

                <h3> ⏲ Horarios de Atención </h3>
                <b><p style="white-space: pre-wrap;">{negocio.horario_atencion}</p></b>
            </div>
    {:else}
        <p class="error"> ⚠ No se pudo cargar la infomacion del negocio. Intenta mas tarde</p>
    {/if}

    <a href="/menu" class="btn-menu">Delivey</a>
</div>


<style>
    img{
        background: none;
        margin: 10px;
        padding: 10px;
        width: 400px;
    }
    h1{color: #000; padding: 10px; background: size 100%;; background-color: #39FF14; border: solid;}
    .contacto-container{
        background: none;
        max-width: 600px;
        margin: 0 auto;
        text-align: center;
    }

    .item h3{
        margin: 0 0 5px 0;
        color: #39FF14;
        font-size: 1.1rem;
    }

    .item p{
        margin: 0;
        font-size: 1.1rem;
        color: #00CCFF;
    }


    .btn-menu{
        color: #000;
        text-decoration: none;
        background-color: #00CCFF;
        padding: 10px 20px ;
        border-radius: 20px;
        display: inline-block;
        text-align: center;
        font-weight: bold;
        transition: background 0,2s;
    }
    .btn-menu:hover{background-color: #39FF14;}
    .destacado{
        background: none; /*Un color sauve para resaltar el horario */
        padding: 10px;
        margin: 10px;
        border-radius: 8px;
        border: 4px dashed #00CCFF;
    }

    .error { color: red; font-weight: bold;}
</style>