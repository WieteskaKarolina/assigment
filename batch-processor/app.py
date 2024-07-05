from flask import Flask, request
from graphene import ObjectType, String, List, Field, Boolean, Schema
from flask_graphql import GraphQLView
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/createBatches": {"origins": "*"}})

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

class ErrorType(ObjectType):
    message = String()

class BatchType(ObjectType):
    batchData = List(String)

class ProcessBatchesResult(ObjectType):
    success = Boolean()
    errors = List(ErrorType)
    batches = List(BatchType)

class Query(ObjectType):
    process_batches = Field(ProcessBatchesResult, records=List(String, required=True))

    def resolve_process_batches(root, info, records):
        print("Processing batches for records:", records)
        processor = BatchProcessor(records)
        batches = processor.process_batches()
        success = True
        errors = []

        batch_objects = [BatchType(batchData=batch) for batch in batches]
        
        return ProcessBatchesResult(success=success, errors=errors, batches=batch_objects)

schema = Schema(query=Query)


app.add_url_rule('/createBatches', view_func=GraphQLView.as_view('createBatches', schema=schema, graphiql=True))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
