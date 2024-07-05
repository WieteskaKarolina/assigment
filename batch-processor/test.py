import unittest
import requests

class TestGraphQL(unittest.TestCase):
    
    base_url = 'http://localhost:5000/graphql'
    
    def test_process_batches(self):
        query = """
        query {
          processBatches(records: ["Record 1", "Record 2", "Record 3"]) {
            success
            errors {
              message
            }
            batches {
              batchData
            }
          }
        }
        """

        response = requests.post(self.base_url, json={'query': query})
        
        print('Status Code:', response.status_code)
        print('Response Text:', response.text)
        
        try:
            result = response.json()
        except ValueError as e:
            self.fail(f"Response is not in JSON format: {e}")
        
        self.assertIn('data', result)
        self.assertNotIn('errors', result)
        data = result['data']['processBatches']
        self.assertIsInstance(data, dict)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['errors'], list)
        self.assertIsInstance(data['batches'], list)
        for batch in data['batches']:
            self.assertIsInstance(batch['batchData'], list)
        
if __name__ == '__main__':
    unittest.main()
