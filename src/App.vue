<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="container">
    <header>
      <div class="wrapper">
        <h1>Stock Search</h1>
        <nav>
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/search">Search</RouterLink>
        </nav>
      </div>
    </header>

    <div class="content">
      <RouterView />
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

header {
  line-height: 1.5;
  max-height: 100vh;
  width: 100%;
  text-align: center;
  display: flex;
  justify-content: center;
  width: 100%;
  top: 0;
  margin-top: 20px;
  margin-bottom: 30px;
  border-bottom: 1px solid var(--color-border);
  padding-bottom: 20px;
}

h1 {
  font-size: 2.5rem;
  color: #2c3e50;
}

nav {
  width: 100%;
  font-size: 1rem;
  text-align: center;
  margin-top: 1.5rem;
}

nav a {
  display: inline-block;
  padding: 0.5rem 1rem;
  margin: 0 0.5rem;
  border-radius: 4px;
  color: #2c3e50;
  text-decoration: none;
  transition: background-color 0.3s;
}

nav a:hover {
  background-color: #e0e0e0;
}

nav a.router-link-active {
  background-color: #42b983;
  color: white;
}

.content {
  width: 100%;
  display: flex;
  justify-content: center;
  align-self: flex-start;
}

@media (max-width: 768px) {
  h1 {
    font-size: 2rem;
  }

  nav {
    font-size: 0.9rem;
  }
}
</style>