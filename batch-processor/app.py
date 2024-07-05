class BatchProcessor:
    MAX_RECORD_SIZE = 1 * 1024 * 1024  # 1 MB in bytes
    MAX_BATCH_SIZE = 5 * 1024 * 1024   # 5 MB in bytes
    MAX_RECORD_COUNT = 500

    def __init__(self, records):
        self.records = records

    def _size_of_record(self, record):
        return len(record.encode('utf-8'))
    
    def process_batches(self):
        batches = []
        current_batch = []
        current_batch_size = 0
        current_record_count = 0

        for record in self.records:
            record_size = self._size_of_record(record)

            if record_size > self.MAX_RECORD_SIZE:
                continue

            if (current_batch_size + record_size <= self.MAX_BATCH_SIZE) and (current_record_count < self.MAX_RECORD_COUNT):
                current_batch.append(record)
                current_batch_size += record_size
                current_record_count += 1
            else:
                batches.append(current_batch)
                current_batch = [record]
                current_batch_size = record_size
                current_record_count = 1

        if current_batch:
            batches.append(current_batch)

        return batches