from processor.screenshot import generate_screenshot_placeholder
from processor.performance import analyze_performance
from processor.image_processor import generate_thumbnails

def test_screenshot():
    b64 = generate_screenshot_placeholder("https://example.com")
    assert isinstance(b64,str) and len(b64)>10

def test_performance():
    perf = analyze_performance("https://example.com")
    assert 'load_time_ms' in perf

def test_thumbnails():
    thumbs = generate_thumbnails("https://example.com")
    assert isinstance(thumbs,list)