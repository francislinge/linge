<template>
	<div id="app" class="">
		<router-view></router-view>
	</div>
</template>

<script>
	export default {
		name: 'app',
		created() {
			
		}
	}
</script>

<style>

	* {
		padding: 0;
		margin: 0;
		box-sizing: border-box;
	}

	html,
	body {
		width: 100%;
		height: 100%;
	}

	#app {
		height: 100%;
	}

	body {
		padding: 0;
		margin: 0;

	}
</style>