export const load = async ({ fetch }) => {
    // 1. Pedimos las hamburguesas
    const resBurgers = await fetch('http://127.0.0.1:8000/api/hamburguesas/');
    const hamburguesas = await resBurgers.json();

    // 2. Pedimos los Extras
    const resProduct = await fetch('http://127.0.0.1:8000/api/Product/');
    const product = await resProduct.json();

    // 3. (Opcional pero recomendado) Pedimos las Categorías
    // Las necesitamos para poder agrupar los extras en el HTML después
    const resCategory = await fetch('http://127.0.0.1:8000/api/Category/');
    const categories = await resCategory.json();

    // 4. Entregamos todo a la página
    return {
        hamburguesas,
        product,
        categories
    };
};