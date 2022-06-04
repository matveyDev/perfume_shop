<template>
	<div class="bg-dark">
		<footer class="footer container">
			<div class="footer__icons">
				<a
					class="icon"
					href="https://www.instagram.com/wonder_de_parfum/"
					target="blank"
				>
					<img src="../source/instagram_logo.png" width="35" alt="Instagram" />
				</a>
			</div>
			<hr class="container text-muted"/>
			<span class="text-muted">© 2022 spicyPerfume, Inc</span>
		</footer>
	</div>
</template>

<script>
export default {};
</script>

<style scoped>
.footer {
  margin-top: 5px;
  padding-top: 35px;
  padding-bottom: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.footer__icons {
  display: flex;
  align-items: center;
}
.icon {
  flex: 1 1 auto;
  margin: 0 5px;
}
hr {
  border: 0,5px solid rgb(206, 206, 206);
}
</style>
