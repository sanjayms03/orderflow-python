def handler(event, context=None):
    # Legacy dependency is imported lazily so the app remains importable without [legacy].
    from PIL import Image
    source = event.get("source_path")
    destination = event.get("destination_path", "/tmp/resized.png")
    image = Image.open(source)
    image.thumbnail((4096, 4096))
    image.save(destination)
    return {"destination": destination, "size": image.size}
