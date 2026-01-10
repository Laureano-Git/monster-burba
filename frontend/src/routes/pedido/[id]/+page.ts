// frontend/src/routes/pedido/[id]/+page.ts

export const load = async ({ fetch, params }) => {
    // 1. Obtener el ID de la hamburguesa de la URL
    const idHamburguesa = params.id; 

    // 2. Cargar la hamburguesa por su ID
    const resBurger = await fetch(`http://127.0.0.1:8000/api/hamburguesas/${idHamburguesa}/`);
    const burger = await resBurger.json();

    // 3. Cargar todas las opciones extra
    const resExtras = await fetch(`http://127.0.0.1:8000/api/OpcionesExtra/`);
    const extras = await resExtras.json();
    
    // 4. Devolver ambos datasets
    return {
        burger,
        extras
    };
};