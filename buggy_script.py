import time

def connect_to_db():
    print("Connecting to database at 192.168.1.100...")
    time.sleep(1)
    print("Connection established.")

def process_data(data_list):
    print(f"Processing {len(data_list)} records...")
    for i, data in enumerate(data_list):
        # A realistic bug: Division by zero when data value is 0
        # This will simulate a "Logic Error" or "Data Issue"
        result = 100 / data
        print(f"Record {i}: processed result {result}")

if __name__ == "__main__":
    print("Starting data processing pipeline...")
    connect_to_db()
    
    # Simulate some valid data followed by a bad record (0)
    dataset = [10, 20, 5, 0, 50]
    
    process_data(dataset)
    print("Processing complete.")
