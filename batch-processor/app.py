class BatchProcessor:
    MAX_RECORD_SIZE = 1 * 1024 * 1024  # 1 MB in bytes
    MAX_BATCH_SIZE = 5 * 1024 * 1024   # 5 MB in bytes
    MAX_RECORD_COUNT = 500

    def __init__(self, records):
        self.records = records

    def _size_of_record(self, record):
        return len(record.encode('utf-8'))