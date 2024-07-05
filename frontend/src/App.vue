<template>
  <div id="app">
    <h1>Batch Processor</h1>
    <textarea v-model="recordsInput" placeholder="Enter records separated by newline"></textarea>
    <button @click="processBatches">Process Batches</button>

    <div v-if="batches.length || loading">
      <h2>Batches</h2>
      <div v-if="loading">Loading batches...</div>
      <ul v-else-if="!batches.length && !errors.length">
        <li>No batches processed yet.</li>
      </ul>
      <div v-for="(batch, index) in batches" :key="index" class="batch">
        <h3>Batch {{ index + 1 }}</h3>
        <ul>
          <li v-for="(record, rIndex) in batch" :key="rIndex">{{ record }}</li>
        </ul>
      </div>
      <div v-if="errors.length">
        <h2>Errors</h2>
        <ul>
          <li v-for="(error, index) in errors" :key="index">{{ error.message }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>