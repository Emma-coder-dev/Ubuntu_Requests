# Ubuntu Image Fetcher

*"I am because we are"* - Ubuntu Philosophy

A Python tool that embodies the Ubuntu spirit of community, respect, and sharing by mindfully collecting images from the global web community.

## 🌍 Ubuntu Principles

This tool implements the core values of Ubuntu:

- **Community**: Connects to the global community of shared resources
- **Respect**: Handles errors gracefully and respects server resources
- **Sharing**: Organizes fetched images for community appreciation
- **Practicality**: Serves real needs while maintaining security

## ✨ Features

### Core Functionality
- ✅ Download images from URLs with respectful HTTP headers
- ✅ Create organized `Fetched_Images` directory
- ✅ Handle multiple URLs in various input formats
- ✅ Graceful error handling for network issues

### Security Features
- 🔒 URL validation (HTTP/HTTPS only)
- 🔒 File size limits (50MB maximum)
- 🔒 Content type validation (images only)
- 🔒 HTTP headers inspection
- 🔒 Safe filename generation

### Advanced Features
- 🔄 Duplicate detection using SHA-256 hashing
- 📁 Automatic filename conflict resolution
- 📊 Download progress tracking
- 🌐 Multiple input methods (single, multi-line, comma-separated)

## 🚀 Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the fetcher:**
   ```bash
   python ubuntu_image_fetcher.py
   ```

## 📖 Usage

### Basic Usage
```bash
python ubuntu_image_fetcher.py
```

The program will guide you through:
1. Choosing input method (single URL, multiple URLs, or comma-separated)
2. Entering image URLs
3. Automatic downloading and organization

### Input Methods

**Option 1: Single URL**
```
Please enter the image URL: https://example.com/image.jpg
```

**Option 2: Multiple URLs (one per line)**
```
Enter URLs (one per line, empty line to finish):
https://example.com/image1.jpg
https://example.com/image2.png
https://example.com/image3.gif
[empty line to finish]
```

**Option 3: Comma-separated URLs**
```
Enter URLs separated by commas: https://example.com/img1.jpg, https://example.com/img2.png
```

## 🛡️ Security Precautions

The Ubuntu Image Fetcher implements several security measures:

### URL Validation
- Only HTTP and HTTPS protocols allowed
- Proper URL format validation
- Domain name verification

### Content Validation
- File size limits (50MB maximum)
- Content type checking (images only)
- HTTP headers inspection
- Safe file extension enforcement

### File Safety
- SHA-256 duplicate detection
- Filename conflict resolution
- Binary mode file writing
- Chunked downloading for large files

## 📁 File Organization

```
Fetched_Images/
├── image1.jpg
├── image2.png
├── ubuntu_image_1234567890.jpg  # Generated filename
└── image1_1.jpg                 # Conflict resolution
```

## 🔧 Technical Details

### HTTP Headers Checked
- `Content-Type`: Ensures image format
- `Content-Length`: Validates file size
- `X-Frame-Options`: Security awareness indicator

### Supported Formats
- JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- BMP (.bmp)
- WebP (.webp)
- SVG (.svg)

### Error Handling
- Connection timeouts
- HTTP errors (404, 403, etc.)
- Invalid URLs
- File system errors
- Network connectivity issues

## 🧪 Testing

Run the test script to verify functionality:

```bash
python test_ubuntu_fetcher.py
```

## 📝 Example Output

```
============================================================
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web
'I am because we are' - Ubuntu Philosophy
============================================================

✓ Community space 'Fetched_Images' is ready

Choose input method:
1. Single URL
2. Multiple URLs (one per line)
3. URLs separated by commas

Enter your choice (1-3): 1
Please enter the image URL: https://example.com/ubuntu-wallpaper.jpg

🌐 Connecting to: https://example.com/ubuntu-wallpaper.jpg
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg
✓ File size: 245760 bytes

Connection strengthened. Community enriched.
```

## 🤝 Contributing

This tool embodies Ubuntu's community spirit. Contributions that enhance:
- Security measures
- Community features
- Respectful web practices
- Error handling

...are welcome and appreciated.

## 📜 License

This project follows the Ubuntu philosophy of sharing and community. Use responsibly and respect the resources of the global web community.

---

*"A person is a person through other persons."* - Ubuntu philosophy

Your program connects you to the work of others across the web, strengthening the bonds of our global community.
