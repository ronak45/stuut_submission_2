
<template>
  <div class="search">
    <h2>Stock Search</h2>
    <input v-model="query" @input="searchStocks" placeholder="Enter stock symbol or name">
    <div v-if="searchResults.length" class="results">
      <div v-for="stock in searchResults" :key="stock.symbol" class="stock-item">
        <h3>{{ stock.symbol }}</h3>
        <p>{{ stock.name }}</p>
        <router-link :to="`/stock/${stock.symbol}`" class="view-details">View Details</router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';
import logger from '@/logger';

const query = ref('');
const searchResults = ref([]);

const searchStocks = async () => {
  if (query.value.length > 1) {
    try {
      console.log('Sending request to:', `/api/search?query=${query.value}`);
      const response = await axios.get(`/api/search?query=${query.value}`);
      console.log('Received response:', response.data);
      searchResults.value = response.data;
    } catch (error) {
      console.error('Error searching stocks:', error);
      if (error.response) {
        console.error('Response data:', error.response.data);
        console.error('Response status:', error.response.status);
      }
    }
  } else {
    searchResults.value = [];
  }
};
</script>

<style scoped>
.search {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
}

h2 {
  text-align: center;
  margin-bottom: 2rem;
}

.search-container {
  margin-bottom: 2rem;
}

input {
  width: 100%;
  padding: 0.8rem;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.results {
  display: grid;
  gap: 1rem;
}

.stock-item {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 1rem;
  background-color: #f9f9f9;
}

.stock-item h3 {
  margin: 0;
  color: #2c3e50;
}

.stock-item p {
  margin: 0.5rem 0;
  color: #34495e;
}

.view-details {
  display: inline-block;
  margin-top: 0.5rem;
  padding: 0.5rem 1rem;
  background-color: #3498db;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-size: 0.9rem;
  transition: background-color 0.3s;
}

.view-details:hover {
  background-color: #2980b9;
}
</style>