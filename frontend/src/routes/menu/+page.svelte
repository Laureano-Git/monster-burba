<script lang="ts">
    import Extras from '$lib/Extras.svelte'
    import HamburguesaCard from '$lib/HamburguesaCard.svelte'
    export let data;
    $: negocio = data.info;
</script>

<main>
    <h1>🍔 Nuestras burgas</h1>

    <div class="menu-grid">
        {#each data.hamburguesas as item}
            <HamburguesaCard burger={item} />
        {/each}
    </div>
    
    <h1>Nuestros Extras y Acompañamientos</h1>
    <div class="menu-product">
        {#each data.categories.filter((c: any) => c.nombre !== 'Hamburguesas') as cat}
            <h2 class="titulo-cat">{cat.nombre}</h2>
            <div class="menu-grid">
                {#each data.product?.filter((e: any) => e.categories === cat.id) ?? [] as item}
                    <Extras product={item}></Extras>
                {:else}
                    <p>No hay productos en esta cagetoria.</p>
                {/each}
            </div>
        {/each}
    </div>
</main>

<style>
    
    main {
        max-width: 1000px;
        margin: 0 auto;
        padding: 20px;
        text-align: center;
    }

    h1 { color: #39FF14; margin-bottom: 40px; }
    h2 { color: #39FF14; margin-bottom: 40px; }

    .menu-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); /* Responsive automático */
        gap: 30px;
    }
    .menu-product{
        display: grid;
        gap: 30px;
    }
</style>