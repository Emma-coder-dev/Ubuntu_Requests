import requests
import os
import hashlib
from urllib.parse import urlparse
from pathlib import Path
import mimetypes
import time
from typing import List, Set

class UbuntuImageFetcher:
    """
    Ubuntu-inspired image fetcher that embodies community, respect, and sharing.
    "I am because we are" - connecting to the global community of shared resources.
    """
    
    def __init__(self):
        self.fetched_dir = "Fetched_Images"
        self.downloaded_hashes: Set[str] = set()
        self.max_file_size = 50 * 1024 * 1024  # 50MB limit for security
        self.allowed_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg'}
        self.allowed_mime_types = {
            'image/jpeg', 'image/jpg', 'image/png', 'image/gif', 
            'image/bmp', 'image/webp', 'image/svg+xml'
        }
        
    def create_directory(self):
        """Create the Fetched_Images directory with Ubuntu spirit."""
        os.makedirs(self.fetched_dir, exist_ok=True)
        print(f"✓ Community space '{self.fetched_dir}' is ready")
    
    def validate_url(self, url: str) -> bool:
        """Validate URL format and protocol for security."""
        try:
            parsed = urlparse(url)
            if not parsed.scheme or parsed.scheme not in ['http', 'https']:
                print("✗ Only HTTP and HTTPS URLs are allowed")
                return False
            if not parsed.netloc:
                print("✗ Invalid URL format")
                return False
            return True
        except Exception:
            print("✗ Invalid URL format")
            return False
    
    def check_http_headers(self, response: requests.Response) -> bool:
        """Check HTTP headers for security and content validation."""
        # Check content type
        content_type = response.headers.get('content-type', '').lower()
        if not any(mime in content_type for mime in self.allowed_mime_types):
            print(f"✗ Unsupported content type: {content_type}")
            return False
        
        # Check content length
        content_length = response.headers.get('content-length')
        if content_length and int(content_length) > self.max_file_size:
            print(f"✗ File too large: {int(content_length)} bytes (max: {self.max_file_size})")
            return False
        
        # Check for suspicious headers
        if 'x-frame-options' in response.headers:
            print("ℹ Security headers detected - source is security-conscious")
        
        return True
    
    def generate_filename(self, url: str, content_type: str) -> str:
        """Generate appropriate filename from URL or content type."""
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename or '.' not in filename:
            # Generate filename based on content type
            extension = mimetypes.guess_extension(content_type.split(';')[0])
            if not extension:
                extension = '.jpg'  # Default fallback
            filename = f"ubuntu_image_{int(time.time())}{extension}"
        
        # Ensure file extension is allowed
        file_ext = Path(filename).suffix.lower()
        if file_ext not in self.allowed_extensions:
            # Replace with safe extension
            safe_ext = mimetypes.guess_extension(content_type.split(';')[0]) or '.jpg'
            filename = Path(filename).stem + safe_ext
        
        return filename
    
    def calculate_file_hash(self, content: bytes) -> str:
        """Calculate SHA-256 hash of file content for duplicate detection."""
        return hashlib.sha256(content).hexdigest()
    
    def is_duplicate(self, content: bytes) -> bool:
        """Check if image is a duplicate based on content hash."""
        file_hash = self.calculate_file_hash(content)
        if file_hash in self.downloaded_hashes:
            return True
        self.downloaded_hashes.add(file_hash)
        return False
    
    def fetch_single_image(self, url: str) -> bool:
        """Fetch a single image with Ubuntu principles of respect and community."""
        try:
            print(f"\n🌐 Connecting to: {url}")
            
            # Validate URL
            if not self.validate_url(url):
                return False
            
            # Create session with respectful headers
            session = requests.Session()
            session.headers.update({
                'User-Agent': 'Ubuntu Image Fetcher - A respectful community tool',
                'Accept': 'image/*',
                'Accept-Encoding': 'gzip, deflate'
            })
            
            # Fetch with timeout and size limits
            response = session.get(url, timeout=15, stream=True)
            response.raise_for_status()
            
            # Check HTTP headers for security
            if not self.check_http_headers(response):
                return False
            
            # Read content in chunks for large files
            content = b''
            for chunk in response.iter_content(chunk_size=8192):
                content += chunk
                if len(content) > self.max_file_size:
                    print("✗ File too large during download")
                    return False
            
            # Check for duplicates
            if self.is_duplicate(content):
                print("ℹ This image has already been shared with our community")
                return True
            
            # Generate filename
            filename = self.generate_filename(url, response.headers.get('content-type', ''))
            filepath = os.path.join(self.fetched_dir, filename)
            
            # Handle filename conflicts
            counter = 1
            original_filepath = filepath
            while os.path.exists(filepath):
                name, ext = os.path.splitext(original_filepath)
                filepath = f"{name}_{counter}{ext}"
                counter += 1
            
            # Save the image
            with open(filepath, 'wb') as f:
                f.write(content)
            
            print(f"✓ Successfully fetched: {os.path.basename(filepath)}")
            print(f"✓ Image saved to {filepath}")
            print(f"✓ File size: {len(content)} bytes")
            
            return True
            
        except requests.exceptions.Timeout:
            print("✗ Connection timeout - the community is patient, try again")
        except requests.exceptions.ConnectionError:
            print("✗ Connection error - unable to reach the community")
        except requests.exceptions.HTTPError as e:
            print(f"✗ HTTP error: {e}")
        except Exception as e:
            print(f"✗ An unexpected error occurred: {e}")
        
        return False
    
    def fetch_multiple_images(self, urls: List[str]) -> None:
        """Fetch multiple images, embodying Ubuntu's community spirit."""
        print(f"\n🤝 Processing {len(urls)} images from our global community...")
        
        successful = 0
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}] Processing...")
            if self.fetch_single_image(url.strip()):
                successful += 1
        
        print(f"\n📊 Community Summary:")
        print(f"✓ Successfully shared: {successful}/{len(urls)} images")
        print(f"✓ Total unique images in community: {len(self.downloaded_hashes)}")
        print("\nConnection strengthened. Community enriched. Ubuntu realized.")
    
    def get_user_urls(self) -> List[str]:
        """Get URLs from user with multiple input options."""
        print("\nChoose input method:")
        print("1. Single URL")
        print("2. Multiple URLs (one per line)")
        print("3. URLs separated by commas")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            url = input("Please enter the image URL: ").strip()
            return [url] if url else []
        
        elif choice == "2":
            print("Enter URLs (one per line, empty line to finish):")
            urls = []
            while True:
                url = input().strip()
                if not url:
                    break
                urls.append(url)
            return urls
        
        elif choice == "3":
            urls_input = input("Enter URLs separated by commas: ").strip()
            return [url.strip() for url in urls_input.split(',') if url.strip()]
        
        else:
            print("Invalid choice, defaulting to single URL")
            url = input("Please enter the image URL: ").strip()
            return [url] if url else []

def main():
    """Main function embodying Ubuntu philosophy."""
    print("=" * 60)
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web")
    print("'I am because we are' - Ubuntu Philosophy")
    print("=" * 60)
    
    fetcher = UbuntuImageFetcher()
    fetcher.create_directory()
    
    # Get URLs from user
    urls = fetcher.get_user_urls()
    
    if not urls:
        print("No URLs provided. Community connection not established.")
        return
    
    # Filter out empty URLs
    urls = [url for url in urls if url]
    
    if len(urls) == 1:
        fetcher.fetch_single_image(urls[0])
    else:
        fetcher.fetch_multiple_images(urls)

if __name__ == "__main__":
    main()
