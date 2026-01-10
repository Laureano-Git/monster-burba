<script>
	//Aquí iría lígica compartida (como saber si el usario esta logeado)
</script>

<div class="app">
	<header>
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.13.1/font/bootstrap-icons.min.css">
		<nav>
			<div class="logo"><a href="/">🦍 MonsterBurgaWeb</a></div>
			<div class="links">
				<a href="/menu">Burgas</a>
			</div>
		</nav>
	</header>

	<main>
		<slot />
	</main>

	<footer>
		<a class="ig" href="https://www.instagram.com/monster.burga/" target="_blank">
			<i class="bi bi-instagram">
				<br>
				instagram
			</i>
		</a>
		<p>&copy; 2025 La Mejor Hamburgeseria - Hecho con SvelteKit & Django</p>
	</footer>
</div>

<style>
	/* Diseño Global de la estructura*/
	:global(body){
		margin: 0;
		font-family: monospace;
		background-color: #000000;
		background-image: url(https://images.unsplash.com/photo-1717851692937-f2ab7adb7630?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D);
		background-repeat: no-repeat;
		background-size: cover;
		background-position: center center;
		background-attachment: fixed;
		/* esta funka, es arena: https://images.pexels.com/photos/952670/pexels-photo-952670.jpeg?cs=srgb&dl=pexels-danielabsi-952670.jpg&fm=jpg*/
	}

	header{
		background-color: #222;
		color: rgb(8, 253, 0);
		padding: 1rem 0;
		box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
	}

	nav{
		max-width: 800px;
		margin: 0 auto;
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 0 20px;
	}

	.logo { font-size: 1.5rem; font-weight: bold;}
	.logo a{text-decoration: none; color: #04fc25;}
	.ig{
		text-decoration: none;
		color: #04fc25;
	}
	.links a {
		color: rgb(8, 253, 0);
		text-decoration: none;
		margin-left: 20px;
		font-weight: 500;
	}

	.links a:hover {color: #08efff;}

	main{
		max-width: 800px;
		margin: 20px auto;
		min-height: 80vh; /*Empuja el footer hacia abajo*/
		padding: 0 20px;
	}

	footer{
		background-color: #000000;
		text-align: center;
		padding: 20px;
		margin-top: 40px;
		color: #04fc25;
	}
</style>