<script lang="ts">
    // Recibimos los datos del archivo +page.ts
    export let burger;
</script>

<div class="card">
    {#if burger.imagen}
        <img src={burger.imagen} alt={burger.nombre} />
    {/if}
            
    <h2>{burger.nombre}</h2>
    <p class="desc">{burger.descripcion}</p>

    <!-- Adicion para ver las categorias -->
    {#if burger.es_oferta}
        <div class="tag_oferta">¡OFERTA!</div>
    {/if}
    <h2>{burger.nombre} a solo:</h2>
    
    <div class="card-footer">
        {#if burger.precio_simple != 0}
            <p class="precio">${burger.precio_simple}</p>
        {/if}
        {#if burger.precio_simple == 0}
            <p class="precio">${burger.precio_doble}</p>
        {/if}

        <a href="/pedido/{burger.id}" class="btn-pedir">
                Perzonalizar y Pedir
        </a>
    </div>
</div>

<style>
    /* Un poco de CSS básico para que no se vea feo */
    .card {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        background: white;
        transition: transform 0.2s; /* Un efectito extra */
    }

    .card:hover {
        transform: translateY(-5px); /* Se levanta al pasar el mouse */
    }
    .card {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }

    img {
        width: 100%;       /* Que ocupe todo el ancho de la tarjeta */
        height: 200px;     /* Altura fija */
        object-fit: cover; /* Recortar la imagen para que no se deforme */
        border-radius: 4px;
    }

    .precio {
        font-weight: bold;
        color: green;
        font-size: 1.2rem;
    }
    .tag_oferta{
        color: green;
    }

    .btn-pedir{
        color: white; /* Esto cambia el color de azul estandar de un link a blanco */
        text-decoration: none; /* Esto quita el subrayado */
        display: inline-block; /* Permite que el boton tenga "cuerpo" (alto y ancho) */
        background-color: #00CCFF;
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: bold;
        text-align: center;
        transition: background 0.2s;
    }

    .btn-pedir:hover{
        background-color: #39FF14;
    }
</style>