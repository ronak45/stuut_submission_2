<template>
  <div class="stock-details" v-if="stockData">
    <h2>{{ stockData.name }} ({{ stockData.symbol }})</h2>
    <div class="price-info">
      <p class="current-price">Current Price: ${{ stockData.currentPrice.toFixed(2) }}</p>
      <p class="price-change" :class="{ positive: priceChange >= 0, negative: priceChange < 0 }">
        {{ priceChange >= 0 ? '+' : '' }}{{ priceChange.toFixed(2) }} ({{ priceChangePercent.toFixed(2) }}%)
      </p>
    </div>
        
    <!-- <div class="charts">
      <div class="chart">
        <h3>Historical Prices</h3>
        <LineChart v-if="historicalPriceChartData" :chart-data="historicalPriceChartData" :options="chartOptions" />
      </div>
      <div class="chart">
        <h3>Volume</h3>
        <BarChart v-if="volumeChartData" :chart-data="volumeChartData" :options="chartOptions" />
      </div>
    </div>
    -->

    <div class="additional-info">
      <h3>Additional Information</h3>
      <p>Open: ${{ stockData.open.toFixed(2) }}</p>
      <p>High: ${{ stockData.dayHigh.toFixed(2) }}</p>
      <p>Low: ${{ stockData.dayLow.toFixed(2) }}</p>
      <p>Volume: {{ stockData.volume.toLocaleString() }}</p>
      <p>Market Cap: ${{ formatMarketCap(stockData.marketCap) }}</p>
      <p>52 Week High: ${{ stockData.fiftyTwoWeekHigh.toFixed(2) }}</p>
      <p>52 Week Low: ${{ stockData.fiftyTwoWeekLow.toFixed(2) }}</p>
    </div>
  </div>
  <div v-else>Loading...</div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import logger from '@/logger';
import { Line as LineChart, Bar as BarChart } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, LinearScale, PointElement, CategoryScale, BarElement } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, LineElement, LinearScale, PointElement, CategoryScale, BarElement);

const route = useRoute();
const stockData = ref(null);
const historicalData = ref([]);

const fetchStockData = async () => {
  try {
    const response = await axios.get(`/api/stock/${route.params.symbol}`);
    console.log('Stock data:', response.data);
    stockData.value = response.data;
    
    // Fetch historical data
    const historicalResponse = await axios.get(`/api/stock/${route.params.symbol}/historical`);
    console.log('Historical data:', historicalResponse.data);
    historicalData.value = historicalResponse.data;
  } catch (error) {
    console.error('Error fetching stock data:', error);
  }
};

onMounted(fetchStockData);

const priceChange = computed(() => {
  if (stockData.value) {
    return stockData.value.currentPrice - stockData.value.previousClose;
  }
  return 0;
});

const priceChangePercent = computed(() => {
  if (stockData.value && stockData.value.previousClose !== 0) {
    return (priceChange.value / stockData.value.previousClose) * 100;
  }
  return 0;
});

const historicalPriceChartData = computed(() => ({
  labels: historicalData.value.map(item => item.date),
  datasets: [{
    label: 'Close Price',
    data: historicalData.value.map(item => item.close),
    borderColor: '#42b983',
    fill: false
  }]
}));

const volumeChartData = computed(() => ({
  labels: historicalData.value.map(item => item.date),
  datasets: [{
    label: 'Volume',
    data: historicalData.value.map(item => item.volume),
    backgroundColor: '#3498db'
  }]
}));

const formatMarketCap = (value) => {
  if (value >= 1e12) return `${(value / 1e12).toFixed(2)}T`;
  if (value >= 1e9) return `${(value / 1e9).toFixed(2)}B`;
  if (value >= 1e6) return `${(value / 1e6).toFixed(2)}M`;
  return value.toLocaleString();
};


const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
};


</script>

<style scoped>
.stock-details {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.price-info {
  display: flex;
  align-items: baseline;
  margin-bottom: 20px;
}

.current-price {
  font-size: 24px;
  font-weight: bold;
  margin-right: 10px;
}

.price-change {
  font-size: 18px;
}

.positive { color: green; }
.negative { color: red; }

.charts {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.chart {
  width: 48%;
}

</style>