export const load = async ({ fetch }) => {
    const res = await fetch('http://127.0.0.1:8000/api/InformacionNegocio/');
    const info = await res.json();
    
    return {
        info // Retornamos el primer objeto de la lista
    };
};