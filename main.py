from mutagen.id3 import ID3

def get_tags(file_path):
    audio = ID3(file_path)
    
    title = audio.get('TIT2', [None])[0]
    
    print(title)


def print_tags(file_path):
    try:
        audio = ID3(file_path)
        for tag in audio.values():
            print(f"{tag.FrameID}: {tag.text}")

    except Exception as e:
        print(f"Errore nel caricamento del file: {e}")


if __name__ == "__main__":
    file_path = "/Users/davideresigotti/Desktop/PIOVE.mp3"
  
    print_tags(file_path)
