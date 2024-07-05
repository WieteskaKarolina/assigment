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

<script>
  import { ref } from 'vue';
  
  export default {
    setup() {
      const recordsInput = ref('');
      const batches = ref([]);
      const errors = ref([]);
      const loading = ref(false);
  
      const processBatches = async () => {
        loading.value = true;
  
        try {
          const result = await fetch('http://localhost:5000/createBanches', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              query: `
                query ProcessBatches($records: [String!]!) {
                  processBatches(records: $records) {
                    success
                    errors {
                      message
                    }
                    batches {
                      batchData
                    }
                  }
                }
              `,
              variables: {
                records: recordsInput.value.split('\n')
              }
            }),
          });
  
          const response = await result.json();
          console.log(response);
  
          if (response.data && response.data.processBatches) {
            const { success, errors: gqlErrors, batches: gqlBatches } = response.data.processBatches;
  
            if (success) {
              batches.value = gqlBatches.map(batch => batch.batchData);
              errors.value = [];
            } else {
              console.error('GraphQL error response:', gqlErrors);
              errors.value = gqlErrors || [{ message: 'Unknown error' }];
              batches.value = [];
            }
          } else {
            console.error('GraphQL response did not contain expected data:', response);
            errors.value = [{ message: 'Unexpected response from server.' }];
            batches.value = [];
          }
        } catch (error) {
          console.error('Error during processing batches:', error);
          errors.value = [{ message: 'An error occurred while processing batches.' }];
        } finally {
          loading.value = false;
        }
      };
  
      return {
        recordsInput,
        batches,
        processBatches,
        loading,
        errors,
      };
    },
  };
  </script>