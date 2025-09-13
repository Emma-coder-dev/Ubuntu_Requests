#!/usr/bin/env python3
"""
Test script for Ubuntu Image Fetcher
Demonstrates the functionality with sample URLs
"""

from ubuntu_image_fetcher import UbuntuImageFetcher

def test_ubuntu_fetcher():
    """Test the Ubuntu Image Fetcher with sample functionality."""
    print("Testing Ubuntu Image Fetcher...")
    
    # Create fetcher instance
    fetcher = UbuntuImageFetcher()
    fetcher.create_directory()
    
    # Test URL validation
    print("\n=== Testing URL Validation ===")
    test_urls = [
        "https://httpbin.org/image/jpeg",  # Valid test URL
        "ftp://invalid.com/image.jpg",     # Invalid protocol
        "not-a-url",                      # Invalid format
        "https://httpbin.org/image/png"   # Another valid test URL
    ]
    
    for url in test_urls:
        is_valid = fetcher.validate_url(url)
        print(f"URL: {url} -> Valid: {is_valid}")
    
    # Test filename generation
    print("\n=== Testing Filename Generation ===")
    test_cases = [
        ("https://example.com/image.jpg", "image/jpeg"),
        ("https://example.com/", "image/png"),
        ("https://example.com/photo", "image/gif")
    ]
    
    for url, content_type in test_cases:
        filename = fetcher.generate_filename(url, content_type)
        print(f"URL: {url} -> Filename: {filename}")
    
    # Test hash calculation
    print("\n=== Testing Duplicate Detection ===")
    test_content1 = b"test image content"
    test_content2 = b"different image content"
    
    hash1 = fetcher.calculate_file_hash(test_content1)
    hash2 = fetcher.calculate_file_hash(test_content2)
    
    print(f"Content 1 hash: {hash1[:16]}...")
    print(f"Content 2 hash: {hash2[:16]}...")
    print(f"Are they different? {hash1 != hash2}")
    
    print("\n=== Ubuntu Image Fetcher Test Complete ===")
    print("The fetcher is ready to connect to the global community!")

if __name__ == "__main__":
    test_ubuntu_fetcher()
