<script lang="ts">
    // Recibimos los datos del archivo +page.ts
    export let product;
</script>

<div class="card">
    {#if product.image}
        <img src={product.image} alt={product.nombre} />
    {/if}
            
    <h2>{product.nombre}</h2>
    <p class="desc">{product.descripcion}</p>

    <!-- Adicion para ver las categorias -->
    {#if product.es_oferta}
        <div class="tag_oferta">¡OFERTA!</div>
    {/if}
    
    <div class="card-footer">
        {#if product.precio != 0}
            <p class="precio">${product.precio}</p>
            <a href="/pedido/{product.id}" class="btn-pedir">
                Pedir
            </a>
        {/if}
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