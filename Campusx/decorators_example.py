import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}...")
        print(f"Arguments: {args}, {kwargs}")
        start_time= time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@log_execution_time
def load_model(model_name):
    print(f"Loading model: {model_name}")
    time.sleep(2)
    return f"{model_name} loaded"


@log_execution_time 
def preprocess_image(image_path, size=224):
    print(f"Preprocessing {image_path} to {size}x{size}")
    time.sleep(1)
    return f"processed_{image_path}"

@log_execution_time
def predict(model, image, threshold=0.5):
    print(f"Running prediction using {model}")
    time.sleep(1.5)

    return {
        "class": "cat",
        "confidence": 0.94,
        "threshold": threshold
    }

@log_execution_time
def generate_embedding(text, dimensions=768):
    print(f"Generating embedding for: {text}")
    time.sleep(0.5)

    return [0.1, 0.2, 0.3]


generated_model = load_model("resnet50")