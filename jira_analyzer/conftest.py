import pytest

# Global test configuration
@pytest.fixture(autouse=True)
def setup_test_environment():
    """Setup that runs before each test"""
    print("\n🧪 Setting up test environment")
    yield
    print("🧹 Cleaning up test environment")