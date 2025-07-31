# src/generator.py

def generate_synthetic_data(prompt: str, model: str = "mock-model") -> list:
    """
    Simulates synthetic data generation by returning mock data.
    """
    # You can expand this with more realistic fields
    mock_data = [
        {
            "timestamp": "2025-07-31T10:00:00Z",
            "location": "San Francisco",
            "vehicle_speed": 45.2,
            "pedestrian_detected": True,
            "lidar_points": 1024,
            "weather": "Clear"
        },
        {
            "timestamp": "2025-07-31T10:00:01Z",
            "location": "San Francisco",
            "vehicle_speed": 44.1,
            "pedestrian_detected": False,
            "lidar_points": 1010,
            "weather": "Clear"
        },
        {
            "timestamp": "2025-07-31T10:00:02Z",
            "location": "San Francisco",
            "vehicle_speed": 46.0,
            "pedestrian_detected": False,
            "lidar_points": 1008,
            "weather": "Cloudy"
        }
    ]
    return mock_data
