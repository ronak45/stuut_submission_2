<template>
  <div class="home">
    <h2>Welcome to Stock Search</h2>
    <p>Use our powerful search tool to find and analyze stocks.</p>
    <router-link to="/search" class="cta-button">Start Searching</router-link>
  </div>
</template>

<script setup lang="ts">
// No setup needed for this simple component
</script>

<style scoped>
.home {
  text-align: center;
  padding: 2rem;
}

h2 {
  font-size: 2rem;
  color: #2c3e50;
  margin-bottom: 1rem;
}

p {
  font-size: 1.2rem;
  color: #34495e;
  margin-bottom: 2rem;
}

.cta-button {
  display: inline-block;
  padding: 0.8rem 1.5rem;
  background-color: #42b983;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-size: 1.1rem;
  transition: background-color 0.3s;
}

.cta-button:hover {
  background-color: #3aa876;
}
</style>